def generate_answer(query, retrieved_chunks):
    context = ""

    for doc in retrieved_chunks["documents"][0][:5]:
        cleaned_doc = doc[:1200]
        context += cleaned_doc + "\n\n"

    prompt = f"""
You are a senior software engineer.

Explain the code clearly and professionally.

Structure your answer:

1. Simple Explanation (brief)
2. Step-by-Step Flow
3. Key Components
4. Summary

Rules:
- Be clear and structured
- Include enough detail to understand the system
- Avoid unnecessary repetition
- If context is partially sufficient, try to give the best possible explanation instead of stopping early. Only say "Not enough information" if nothing useful is found.

Context:
{context}

Question: {query}
""" 

    return prompt