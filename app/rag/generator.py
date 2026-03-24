def generate_answer(query, retrieved_chunks):
    context = ""

    for doc in retrieved_chunks["documents"][0]:
        context += doc + "\n\n"

    prompt = f"""
You are a senior software engineer.

Explain the code clearly and step-by-step.

Context:
{context}

Question: {query}

Give a clean and structured answer.
"""

    return prompt