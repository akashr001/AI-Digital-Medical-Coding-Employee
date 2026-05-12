import os
import time

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")

def call_llm(system_prompt: str, user_query: str):

    retries = 3

    for attempt in range(retries):

        try:

            response = completion(
                model="ollama/llama3.1:8b",
                api_base=OLLAMA_BASE_URL,
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            )

            return response["choices"][0]["message"]["content"]

        except Exception as e:

            print(f"Retry failed: {e}")

            time.sleep(2)

    raise Exception("LLM failed")