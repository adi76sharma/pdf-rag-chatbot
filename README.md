# PDF RAG Chatbot

An AI-powered PDF chatbot built using Retrieval Augmented Generation (RAG).

This project allows users to:

- Upload PDF documents
- Ask questions from PDFs
- Retrieve semantic answers using embeddings and vector search
- Generate AI answers using Groq LLM

---

# Features

- PDF Upload
- Text Extraction
- Chunking Pipeline
- HuggingFace Embeddings
- Chroma Vector Database
- Semantic Search
- AI-generated Answers
- Streamlit Chat UI
- FastAPI Backend

---

# Tech Stack

## Backend
- FastAPI
- LangChain
- ChromaDB
- PyMuPDF

## Frontend
- Streamlit

## AI/LLM
- HuggingFace Embeddings
- Groq LLM

---

# Project Structure

```bash
pdf-rag/
│
├── backend/
│   ├── app.py
│   ├── embeddings.py
│   ├── ingest.py
│   └── query.py
│
├── frontend/
│   └── streamlit_app.py
│
├── uploads/
├── chroma_db/
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-chatbot.git
```

---

# Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_api_key
```

---

# Run Backend

```bash
cd backend
uvicorn app:app --reload
```

---

# Run Frontend

```bash
cd frontend
streamlit run streamlit_app.py
```

---

# Future Improvements

- Multi-PDF Support
- Citations & Page Numbers
- Chat Memory
- Hybrid Retrieval
- Agentic RAG
- Qdrant Integration
- Streaming Responses

---

# Author

Aditya Sharma