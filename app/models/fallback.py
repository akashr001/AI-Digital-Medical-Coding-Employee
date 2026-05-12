from litellm import completion

def fallback_completion(messages):

    try:

        response = completion(
            model="ollama/llama3.1:8b",
            messages=messages
        )

        return response

    except Exception:

        response = completion(
            model="ollama/mistral:7b",
            messages=messages
        )

        return response