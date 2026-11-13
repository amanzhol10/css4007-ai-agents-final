import sys
from llm_client import ask, LLMError


def main():
    question = " ".join(sys.argv[1:]).strip()
    if not question:
        print('Usage: python src/main.py "your question"')
        return 1
    try:
        print(ask(question))
    except LLMError as e:
        print(f"Error: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
