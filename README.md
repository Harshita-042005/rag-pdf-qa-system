📚 Multi-Document Question Answering System using RAG

An intelligent PDF-based Question Answering System built with Streamlit, LangChain, and Hugging Face.
This application allows users to upload multiple PDF documents and generate context-aware answers and summaries using Retrieval-Augmented Generation (RAG).

🚀 Overview

This project implements a Multi-Document QA System that:

Accepts multiple PDF uploads
Extracts and processes text
Performs semantic search using embeddings
Retrieves relevant document chunks
Generates accurate answers using an LLM

The system ensures that responses are generated strictly from the uploaded documents, improving reliability and transparency.

🏗️ Architecture

PDF Upload
   ↓
Text Extraction (PyPDFLoader)
   ↓
Chunking (RecursiveCharacterTextSplitter)
   ↓
Embeddings (all-MiniLM-L6-v2)
   ↓
FAISS Vector Database
   ↓
User Question
   ↓
Relevant Chunk Retrieval
   ↓
LLM (FLAN-T5)
   ↓
Answer / Summary (Streamlit UI)


✨ Features

📄 Upload one or multiple PDF documents
🔍 Semantic search using FAISS vector database
🤖 Retrieval-Augmented Generation (RAG)
🧠 Context-based AI answers
✂️ Smart question splitting using “and”
📝 4-sentence structured document summaries
📊 View retrieved context for transparency
⚡ Interactive web UI using Streamlit
⚙️ Tech Stack

Frontend: Streamlit
Backend: Python
Framework: LangChain
Embeddings: all-MiniLM-L6-v2 (Hugging Face)
LLM: google/flan-t5-base
Vector Database: FAISS
PDF Loader: PyPDFLoader

📂 Project Structure
├── app.py              # Main application
├── requirements.txt    # Dependencies
└── README.md           # Documentation


🛠️ Installation
Clone the repository:
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install dependencies:
pip install -r requirements.txt
▶️ Running the App
streamlit run app.py

Open in browser:
http://localhost:8501


🧠 How It Works
1. Document Processing
PDFs are loaded using PyPDFLoader
Text is split into smaller chunks
Embeddings are created using Hugging Face model
2. Retrieval
FAISS stores vector embeddings
Relevant chunks are retrieved based on the query
3. Answer Generation
LLM generates answers using ONLY retrieved context
Ensures factual accuracy from documents
4. Summarization
Generates exact 4-sentence summaries
Removes repetition and keeps clarity


❓ Usage
Upload one or more PDF documents
Wait for processing
Enter your question
Click "Generate Answer"
Click "Generate Combined Summary" for summaries
Expand "View Retrieved Context" to see source data


⚠️ Limitations
Works best with text-based PDFs
Limited by smaller LLM (FLAN-T5)
Not optimized for very large documents


🔮 Future Improvements
Add OCR for scanned PDFs
Use advanced LLMs (GPT / LLaMA)
Add chat history & conversational memory
Deploy on cloud platforms

🤝 Acknowledgements
Hugging Face
LangChain
Streamlit

📜 License
This project is for educational purposes and can be used or modified freely.
