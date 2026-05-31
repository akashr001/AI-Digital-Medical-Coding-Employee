from app.models.llm import call_llm

print("Calling LLM...")

response = call_llm(
    system_prompt="You are a helpful assistant.",
    user_query="Say hello"
)

print(response)