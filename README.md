# Multi-Document Question Answering System using RAG

## 📌 Project Overview

This project is a Multi-Document Question Answering System built using Python, LangChain, HuggingFace, FAISS, and Streamlit. It allows users to upload multiple PDF documents, extract their content, and ask questions based on the uploaded files.

The system uses Retrieval-Augmented Generation (RAG) to provide accurate, context-based answers by retrieving relevant document chunks and passing them to a language model for response generation.

---

## 🚀 Features

* Upload and process multiple PDF documents
* Semantic search using FAISS vector database
* Retrieval-Augmented Generation (RAG)
* Accurate context-based answers
* Automatic document summarization (4 sentences per document)
* Combined question handling using "and" splitting
* Transparent context display for answers
* Interactive Streamlit web interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Transformers
* Sentence Transformers (all-MiniLM-L6-v2)
* Flan-T5 Language Model

---

## 📂 Project Structure

```
Multi-Document-QA-RAG/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/Multi-Document-QA-RAG.git
cd Multi-Document-QA-RAG
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User uploads one or more PDF documents
2. Text is extracted using PyPDFLoader
3. Documents are split into smaller chunks
4. Embeddings are generated using HuggingFace models
5. FAISS stores the vector representations
6. User enters a question
7. Relevant chunks are retrieved
8. Flan-T5 generates the final answer

---


## 🎯 Use Cases

* Document-based Question Answering
* Research Paper Analysis
* Academic Assistants
* Knowledge Retrieval Systems

---

## 📢 Future Improvements

* Support more file formats (DOCX, TXT)
* Add chatbot-style interaction
* Improve UI/UX design
* Deploy as a cloud application

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* HuggingFace
* FAISS
* Streamlit
