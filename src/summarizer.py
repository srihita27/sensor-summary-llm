import ollama
from src.prompt_template import build_prompt

MODEL = "qwen2.5:0.5b"

def summarize(row):
    prompt = build_prompt(row)

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]