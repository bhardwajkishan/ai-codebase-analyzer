from app.ingestion.repo_loader import clone_repo
from app.ingestion.file_reader import read_code_files
from app.embeddings.chunker import chunk_code
from app.embeddings.embedder import generate_embeddings
from app.embeddings.vector_store import store_embeddings

repo_url = "https://github.com/psf/requests"

repo_path = clone_repo(repo_url)
files = read_code_files(repo_path)

chunks = chunk_code(files)
print(f"Total chunks: {len(chunks)}")

chunks = generate_embeddings(chunks)
print("Embeddings generated")

store_embeddings(chunks)
print("Stored in vector DB")