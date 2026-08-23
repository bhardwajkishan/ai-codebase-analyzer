from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_final_answer(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview",   # stable model
        contents=prompt,
        config={
            "max_output_tokens": 1200,   # limit output length
            "temperature": 0.3          # make answers more accurate & less random
        }
    )

    return response.text