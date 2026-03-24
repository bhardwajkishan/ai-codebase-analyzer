import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(name="codebase")

def store_embeddings(chunks):
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk["content"]],
            embeddings=[chunk["embedding"].tolist()],
            metadatas=[{"file_path": chunk["file_path"]}],
            ids=[str(i)]
        )