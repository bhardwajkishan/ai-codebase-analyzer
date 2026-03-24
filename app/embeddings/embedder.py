from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(chunks):
    for chunk in chunks:
        embedding = model.encode(chunk["content"])
        chunk["embedding"] = embedding

    return chunks