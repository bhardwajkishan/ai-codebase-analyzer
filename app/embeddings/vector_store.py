import hashlib

import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(name="codebase")

def store_embeddings(chunks):
    for chunk in chunks:
        chunk_id = hashlib.sha256(
            f"{chunk['file_path']}:{chunk['content']}".encode("utf-8")
        ).hexdigest()

        collection.upsert(
            documents=[chunk["content"]],
            embeddings=[chunk["embedding"].tolist()],
            metadatas=[{"file_path": chunk["file_path"]}],
            ids=[chunk_id]
        )