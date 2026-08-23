from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.ingestion.repo_loader import clone_repo
from app.ingestion.file_reader import read_code_files
from app.embeddings.chunker import chunk_code
from app.embeddings.embedder import generate_embeddings
from app.embeddings.vector_store import store_embeddings

app = FastAPI(title="AI Codebase Analyzer")


class IndexRequest(BaseModel):
    repo_url: str


class AskRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/index")
def index_repo(request: IndexRequest):
    try:
        repo_path = clone_repo(request.repo_url)
        files = read_code_files(repo_path)

        chunks = chunk_code(files)
        chunks = generate_embeddings(chunks)
        store_embeddings(chunks)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"repo_url": request.repo_url, "chunks_indexed": len(chunks)}


@app.post("/ask")
def ask_question(request: AskRequest):
    from app.rag.retriever import retrieve_relevant_chunks
    from app.rag.generator import generate_answer
    from app.rag.llm import generate_final_answer

    try:
        results = retrieve_relevant_chunks(request.query)
        prompt = generate_answer(request.query, results)
        answer = generate_final_answer(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"query": request.query, "answer": answer}
