from chains.research import run_research
from chains.chat import run_chat
from chains.structured_output import run_structured_output
from chains.streaming import run_streaming
from chains.batch import run_batch
from chains.fallback import run_fallback

MENU = """
Choose a demo:
  1 — Research Report      (Sequential Chain → RunnablePassthrough.assign → RunnableParallel → RunnableLambda)
  2 — Batch Processing     (.batch — run one chain on 3 topics concurrently)
  3 — Chat with Memory     (MessagesPlaceholder + HumanMessage/AIMessage history)
  4 — Structured Output    (PydanticOutputParser — LLM text → typed Python object)
  5 — Streaming            (.stream — token-by-token output)
  6 — Fallback Chain       (.with_fallbacks — auto-retry with a backup model)
  q — Quit
"""

def main():
    while True:
        print(MENU)
        choice = input("> ").strip()

        if choice == "1":
            topic = input("Enter a topic: ").strip()
            if topic:
                try:
                    print(run_research(topic))
                except Exception as e:
                    print(f"Error: {e}")

        elif choice == "2":
            run_batch()

        elif choice == "3":
            run_chat()

        elif choice == "4":
            run_structured_output()

        elif choice == "5":
            run_streaming()

        elif choice == "6":
            run_fallback()

        elif choice.lower() == "q":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
