import streamlit as st
from transformers import pipeline
import re

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import FAISS

st.set_page_config(page_title="Multi-Document QA System", layout="wide")

st.title("📚 Multi-Document Question Answering System (RAG)")
st.markdown("Upload multiple PDFs and generate answers and summaries.")

# -----------------------------
# Session State Initialization
# -----------------------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "all_chunks" not in st.session_state:
    st.session_state.all_chunks = None

if "last_answer" not in st.session_state:
    st.session_state.last_answer = None

if "document_summary" not in st.session_state:
    st.session_state.document_summary = None

if "llm" not in st.session_state:
    st.session_state.llm = None


# -----------------------------
# Document Processing
# -----------------------------
def process_documents(files):
    all_documents = []

    for file in files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        loader = PyPDFLoader(file.name)
        documents = loader.load()
        all_documents.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(all_documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunks, embeddings)

    return vector_db, chunks


# -----------------------------
# Answer Generation
# -----------------------------
def generate_single_answer(question, vector_db, llm):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])
    context = re.sub(r"\[[^\]]*\]", "", context)

    prompt = f"""
    You are an academic assistant.

    Using ONLY the context below, write a clear 4 sentence explanation.
    Do not repeat sentences.
    If information is not available, say:
    "Information not available in the uploaded documents."

    Context:
    {context}

    Question:
    {question}
    """

    answer = llm.invoke(prompt)
    answer = re.sub(r"\[[^\]]*\]", "", answer)

    return answer.strip(), docs


def generate_answer(question, vector_db, llm):
    if " and " in question.lower():
        parts = question.split(" and ")
        combined_answer = ""
        all_docs = []

        for part in parts:
            ans, docs = generate_single_answer(part.strip(), vector_db, llm)
            combined_answer += ans + "\n\n"
            all_docs.extend(docs)

        return combined_answer.strip(), all_docs
    else:
        return generate_single_answer(question, vector_db, llm)


# -----------------------------
# Load LLM (ONLY WHEN NEEDED)
# -----------------------------
@st.cache_resource
def load_model():
    pipe = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",   # ✅ Better quality
        max_new_tokens=150
    )
    return HuggingFacePipeline(pipeline=pipe)


# -----------------------------
# Upload PDFs
# -----------------------------
uploaded_files = st.file_uploader(
    "Upload one or more PDF documents",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files and st.session_state.vector_db is None:
    with st.spinner("Processing documents..."):
        vector_db, chunks = process_documents(uploaded_files)
        st.session_state.vector_db = vector_db
        st.session_state.all_chunks = chunks

    st.success("Documents processed successfully!")


# -----------------------------
# Question & Summary Section
# -----------------------------
if st.session_state.vector_db is not None:

    # Load model lazily
    if st.session_state.llm is None:
        with st.spinner("Loading AI model..."):
            st.session_state.llm = load_model()

    llm = st.session_state.llm

    question = st.text_input("Enter your question:")

    col1, col2 = st.columns(2)

    # -------- Generate Answer --------
    with col1:
        if st.button("Generate Answer") and question:
            with st.spinner("Generating answer..."):
                answer, docs = generate_answer(
                    question,
                    st.session_state.vector_db,
                    llm
                )
                st.session_state.last_answer = (answer, docs)

    # -------- Generate Summary --------
    with col2:
        if st.button("Generate Combined Summary"):

            if st.session_state.all_chunks:

                with st.spinner("Generating summary..."):

                    doc_groups = {}

                    for chunk in st.session_state.all_chunks:
                        source = chunk.metadata.get("source", "unknown")

                        if source not in doc_groups:
                            doc_groups[source] = []

                        doc_groups[source].append(chunk.page_content)

                    summaries_output = ""

                    for source in doc_groups:

                        # Take more content for better summary
                        text = "\n\n".join(doc_groups[source][:5])
                        text = re.sub(r"\[[^\]]*\]", "", text)

                        prompt = f"""
                        Summarize the following document.

                        Write exactly 4 clear sentences.
                        Avoid repetition.
                        Use simple academic language.

                        {text}
                        """

                        summary = llm.invoke(prompt)
                        summary = re.sub(r"\[[^\]]*\]", "", summary)

                        # Remove repeated sentences
                        sentences = summary.split(".")
                        unique_sentences = []

                        for s in sentences:
                            s = s.strip()
                            if s and s not in unique_sentences:
                                unique_sentences.append(s)

                        cleaned_summary = ". ".join(unique_sentences[:4]) + "."

                        summaries_output += f"### Summary of {source}\n\n"
                        summaries_output += cleaned_summary + "\n\n"

                    st.session_state.document_summary = summaries_output


# -----------------------------
# Display Answer
# -----------------------------
if st.session_state.last_answer:
    answer, docs = st.session_state.last_answer

    st.subheader("Answer")
    st.write(answer)

    with st.expander("View Retrieved Context"):
        for doc in docs:
            st.write(doc.page_content)
            st.markdown("---")


# -----------------------------
# Display Summary
# -----------------------------
if st.session_state.document_summary:
    st.subheader("Combined Document Summary")
    st.markdown(st.session_state.document_summary)