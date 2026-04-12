from langchain_core.output_parsers import StrOutputParser

from config import llm
from prompts.constants import streaming_prompt

streaming_chain = streaming_prompt | llm | StrOutputParser()

def run_streaming():
    """Stream a short story token-by-token to the console."""
    print("\n  Streaming Demo — tokens appear as the model generates them.\n")

    topic = input("Enter a story topic: ").strip()
    if not topic:
        return

    print()
    try:
        # .stream() yields string chunks instead of one big response
        for chunk in streaming_chain.stream({"topic": topic}):
            print(chunk, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\nError: {e}\n")
