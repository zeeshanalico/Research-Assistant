from langchain_core.output_parsers import StrOutputParser

from config import llm, fallback_llm
from prompts.constants import fallback_prompt

parser = StrOutputParser()

primary_chain = fallback_prompt | llm | parser
backup_chain = fallback_prompt | fallback_llm | parser

# If primary_chain fails (timeout, rate-limit, etc.), backup_chain runs instead.
fallback_chain = primary_chain.with_fallbacks([backup_chain])


def run_fallback():
    """Demo the fallback mechanism — tries primary model, falls back if needed."""
    print("\n  Fallback Demo")
    print(f"  Primary model  → tries first")
    print(f"  Fallback model → catches errors automatically\n")

    user_input = input("Ask anything: ").strip()
    if not user_input:
        return

    try:
        result = fallback_chain.invoke({"input": user_input})
        print(f"\nAI: {result}\n")
    except Exception as e:
        print(f"Both models failed: {e}\n")
