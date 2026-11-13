import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

load_dotenv()


class LLMError(Exception):
    pass


def get_client():
    api_key = os.getenv("LLM_API_KEY")
    if not api_key:
        raise LLMError("LLM_API_KEY is not set")
    return OpenAI(api_key=api_key)


def ask(question, system_prompt="You are a helpful assistant for university students."):
    model = os.getenv("LLM_MODEL")
    if not model:
        raise LLMError("LLM_MODEL is not set")
    client = get_client()
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )
    except OpenAIError as e:
        raise LLMError(f"LLM request failed: {e}") from e
    content = response.choices[0].message.content
    if not content:
        raise LLMError("LLM returned an empty answer")
    return content.strip()
