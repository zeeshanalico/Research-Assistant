from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

from config import llm
from prompts.constants import chat_prompt

chat_chain = chat_prompt | llm | StrOutputParser()

def run_chat():
    """Interactive chat loop — history grows each turn so the model
    remembers earlier messages."""
    history = []
    print("\n  Chat mode (type 'back' to return to menu)\n")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() in ("back", "quit", "q"):
            break

        try:
            reply = chat_chain.invoke({"input": user_input, "history": history})
            print(f"AI: {reply}\n")

            # Append AFTER a successful response so failed calls don't pollute history.
            history.append(HumanMessage(content=user_input))
            history.append(AIMessage(content=reply))
        except Exception as e:
            print(f"Error: {e}\n")
