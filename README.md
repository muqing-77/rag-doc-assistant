
# RAG Document Assistant

A lightweight Retrieval-Augmented Generation (RAG) document assistant built with Python, LangChain, OpenAI embeddings, ChromaDB, and Streamlit.

This project demonstrates how to build an AI system that answers questions grounded in external documents instead of relying only on a model’s internal knowledge.

---

## Overview

Traditional LLMs may hallucinate or fail to answer questions about private or domain-specific documents.

This project solves that problem by using a Retrieval-Augmented Generation (RAG) pipeline:

1. Load documents from local files
2. Split them into smaller chunks
3. Convert chunks into embeddings
4. Store them in a vector database
5. Retrieve the most relevant chunks for a user query
6. Generate answers using an LLM grounded in retrieved context

---

## Demo Workflow


Document -> Chunking -> Embedding -> Vector Store
                              ↓
User Question -> Semantic Retrieval -> LLM Answer
## Features

- Document ingestion pipeline
- Text chunking
- Embedding generation with OpenAI
- Vector storage using ChromaDB
- Semantic search
- Question answering using an LLM

---

## Project Structure
rag-doc-assistant/
├── data/
│   └── sample.txt
├── app.py
├── ingest.py
├── query.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env.example


---


---

## How It Works

The pipeline consists of three main steps.

### 1. Document Ingestion

`ingest.py` loads documents from the `data/` directory, splits them into smaller chunks, generates embeddings, and stores them in a Chroma vector database.
python ingest.py


---

### 2. Retrieval

When a user asks a question, the system converts the query into an embedding and performs semantic search in the vector database.

---

### 3. Answer Generation

The retrieved document chunks are passed to a large language model, which generates a context-aware response.
python query.py


---

## Installation

Clone the repository:
git clone https://github.com/YOUR_USERNAME/rag-doc-assistant.git

cd rag-doc-assistant

git clone https://github.com/YOUR_USERNAME/rag-doc-assistant.git

cd rag-doc-assistant
conda create -n rag-assistant python=3.10
conda activate rag-assistant



Install dependencies:
pip install -r requirements.txt


Create `.env` file:
OPENAI_API_KEY=your_api_key_here


---

## Example Use Cases

This architecture is widely used in:

- enterprise knowledge assistants
- document question answering
- internal company documentation search
- customer support AI agents
- research paper analysis tools

---

## Technologies Used

- Python
- LangChain
- OpenAI API
- Chroma Vector Database
- Streamlit

---

## Future Improvements

- PDF upload support
- multi-document knowledge base
- chat-style interface
- citation sources in answers
