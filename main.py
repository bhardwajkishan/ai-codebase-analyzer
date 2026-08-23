import argparse

from dotenv import load_dotenv

from app.ingestion.repo_loader import clone_repo
from app.ingestion.file_reader import read_code_files
from app.embeddings.chunker import chunk_code
from app.embeddings.embedder import generate_embeddings
from app.embeddings.vector_store import store_embeddings

load_dotenv()


def index(repo_url):
    repo_path = clone_repo(repo_url)
    files = read_code_files(repo_path)

    chunks = chunk_code(files)
    print(f"Total chunks: {len(chunks)}")

    chunks = generate_embeddings(chunks)
    print("Embeddings generated")

    store_embeddings(chunks)
    print("Stored in vector DB")


def ask(query):
    from app.rag.retriever import retrieve_relevant_chunks
    from app.rag.generator import generate_answer
    from app.rag.llm import generate_final_answer

    results = retrieve_relevant_chunks(query)
    prompt = generate_answer(query, results)
    answer = generate_final_answer(prompt)
    print(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Codebase Analyzer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    index_parser = subparsers.add_parser("index", help="Clone and index a GitHub repo")
    index_parser.add_argument("repo_url")

    ask_parser = subparsers.add_parser("ask", help="Ask a question about the indexed repo")
    ask_parser.add_argument("query")

    args = parser.parse_args()

    if args.command == "index":
        index(args.repo_url)
    elif args.command == "ask":
        ask(args.query)
