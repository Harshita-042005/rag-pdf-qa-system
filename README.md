📚 Multi-Document Question Answering System (RAG)

A Streamlit-based application that allows users to upload multiple PDF documents and perform question answering and summarization using Retrieval-Augmented Generation (RAG).

🚀 Features
📄 Upload multiple PDF documents
🔍 Semantic search using vector embeddings (FAISS)
🤖 AI-powered question answering (FLAN-T5)
🧠 Context-aware responses using retrieved chunks
📝 Automatic document summarization
⚡ Fast and interactive UI with Streamlit
🏗️ Tech Stack
Frontend: Streamlit
LLM: Hugging Face (google/flan-t5-base)
Embeddings: Sentence Transformers (all-MiniLM-L6-v2)
Vector Store: FAISS
Framework: LangChain
📂 Project Structure
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
⚙️ Installation
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
▶️ Usage

Run the Streamlit app:

streamlit run app.py

Then open the local URL shown in your terminal.

🧠 How It Works
Upload PDFs
Documents are loaded using PyPDFLoader
Chunking
Text is split into smaller chunks using RecursiveCharacterTextSplitter
Embedding
Each chunk is converted into vector embeddings
Storage
Stored in FAISS vector database
Retrieval + Generation (RAG)
Relevant chunks are retrieved based on the query
LLM generates answers using only retrieved context
❓ Features Explained
🔹 Question Answering
Supports multi-part questions (splits on "and")
Generates concise 4-sentence answers
Uses only retrieved document context
🔹 Document Summarization
Generates summaries per document
Removes repetition
Outputs structured summaries
📸 Demo (Optional)

Add screenshots or GIFs here

🛠️ Dependencies

From requirements.txt:

streamlit
langchain
langchain-community
langchain-huggingface
faiss-cpu
sentence-transformers
pypdf
⚠️ Limitations
Works best with text-based PDFs (not scanned images)
Limited context window due to small model
Summaries are based on partial document chunks
🔮 Future Improvements
Add support for scanned PDFs (OCR)
Use more powerful LLMs (e.g., GPT / LLaMA)
Add chat history / conversational memory
Deploy on cloud (Streamlit Cloud / AWS)
🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

📜 License

This project is open-source and available under the MIT License.
