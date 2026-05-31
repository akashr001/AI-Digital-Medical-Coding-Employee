import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)

MODEL_NAME = os.getenv(
    "NVIDIA_MODEL",
    "minimaxai/minimax-m2.7"
)


def call_llm(
    system_prompt: str,
    user_query: str
) -> str:

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_query
            }
        ],
        temperature=0.2,
        top_p=0.95,
        max_tokens=8192,
        stream=False
    )

    return completion.choices[0].message.content