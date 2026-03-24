# AI Codebase Understanding System

An AI-powered system that can analyze any GitHub repository and answer questions about the codebase using RAG (Retrieval-Augmented Generation).

## Features
- Code ingestion from GitHub
- Semantic search using embeddings
- Vector database (ChromaDB)
- AI-powered answers using Gemini

## Tech Stack
- Python
- FastAPI (planned)
- ChromaDB
- Sentence Transformers
- Gemini LLM

## How It Works
1. Clone repository
2. Convert code into chunks
3. Generate embeddings
4. Store in vector DB
5. Retrieve relevant code
6. Generate answer using LLM

## Run Project
```bash
python test_rag.py