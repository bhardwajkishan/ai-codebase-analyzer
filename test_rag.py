from dotenv import load_dotenv
load_dotenv()

from app.rag.retriever import retrieve_relevant_chunks
from app.rag.generator import generate_answer
from app.rag.llm import generate_final_answer

query = "Explain the architecture of this repository"

results = retrieve_relevant_chunks(query)

prompt = generate_answer(query, results)

final_answer = generate_final_answer(prompt)

print(final_answer)