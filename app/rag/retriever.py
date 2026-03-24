import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(name="codebase")

def retrieve_relevant_chunks(query, n_results=5):
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )

    return results