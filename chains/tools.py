from langchain_core.tools import tool
# from langchain.tools import tool, ToolRuntime

from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

from config import llm
from prompts.constants import TOOLS_SYSTEM

# ── Tool Definitions ─────────────────────────────────────────────────────────

@tool
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b

@tool
def word_count(text: str) -> int:
    """Count the number of words in a text string."""
    return len(text.split())

TOOLS = [add, multiply, word_count]
TOOL_MAP = {t.name: t for t in TOOLS}

# Bind tools to the LLM so it knows what's available
llm_with_tools = llm.bind_tools(TOOLS)


def run_tools():
    """Demo tool calling — LLM decides which tools to call, results are fed back."""
    print("\n  Tool Calling Demo")
    print("  Available tools: add, multiply, word_count")
    print("  Example: 'What is 38 multiplied by 4?' or")
    print("           'How many words are in the phrase: the quick brown fox?'\n")

    user_input = input("Ask something: ").strip()
    if not user_input:
        return

    messages = [
        SystemMessage(content=TOOLS_SYSTEM),
        HumanMessage(content=user_input),
    ]

    try:
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        while response.tool_calls:
            for tc in response.tool_calls:
                tool_fn = TOOL_MAP[tc["name"]]
                result = tool_fn.invoke(tc["args"])
                print(f"  [tool] {tc['name']}({tc['args']}) → {result}")
                messages.append(
                    ToolMessage(content=str(result), tool_call_id=tc["id"])
                )

            # ── Turn N: LLM reads tool results and produces final answer ──────
            response = llm_with_tools.invoke(messages)
            messages.append(response)

        print(f"\nAI: {response.content}\n")

    except Exception as e:
        print(f"Error: {e}\n")
