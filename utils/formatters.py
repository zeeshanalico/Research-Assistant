"""
Custom Python functions wrapped as RunnableLambda helpers.

Concept demonstrated:
  - RunnableLambda : turns any Python function into a chain-compatible step
"""

from langchain_core.runnables import RunnableLambda


# ── Raw functions ────────────────────────────────────────────────────────────

def format_research_report(data: dict) -> str:
    """Combine key_points + summary + quiz into a nice report string."""
    divider = "=" * 50
    return (
        f"\n{divider}"
        f"\n  RESEARCH REPORT"
        f"\n{divider}"
        f"\n\nKEY POINTS:\n{data['key_points']}"
        f"\n\nSUMMARY:\n{data['summary']}"
        f"\n\nQUIZ:\n{data['quiz']}"
        f"\n{divider}\n"
    )


def wrap_in_dict(key: str):
    """Return a function that wraps a plain value into {key: value}.
    Useful after a chain that outputs a string but the next step needs a dict."""
    def _wrap(value):
        return {key: value}
    return _wrap


# ── RunnableLambda wrappers (plug directly into chains with |) ──────────────

report_formatter = RunnableLambda(format_research_report)
wrap_as_key_points = RunnableLambda(wrap_in_dict("key_points"))
