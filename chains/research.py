from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config import llm
from prompts.constants import key_points_prompt, summary_prompt, quiz_prompt
from utils.formatters import report_formatter, wrap_as_key_points

parser = StrOutputParser()

# ── Sub-chains ───────────────────────────────────────────────────────────────

key_points_chain = key_points_prompt | llm | parser
summary_chain = summary_prompt | llm | parser
quiz_chain = quiz_prompt | llm | parser

full_research_chain = (
    key_points_chain                        # {"topic": ...} → str
    | wrap_as_key_points                    # str → {"key_points": str}
    | RunnablePassthrough.assign(           # keeps key_points, adds summary & quiz
        summary=summary_chain,              # runs in parallel ──┐
        quiz=quiz_chain,                    # runs in parallel ──┘
    )
    | report_formatter                      # dict → formatted string
)


def run_research(topic: str) -> str:
    """Invoke the full research chain end-to-end."""
    print(f"  Generating research report for '{topic}'...")
    print("  (key points → summary + quiz in parallel → format)\n")
    return full_research_chain.invoke({"topic": topic})
