import os
from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter
from langchain_core.globals import set_llm_cache
from langchain_core.caches import InMemoryCache

load_dotenv()

# If you invoke the same prompt twice, the second call returns instantly from cache instead of hitting the API again.
set_llm_cache(InMemoryCache())

# ── Model Constants ─────────────────────────────────────────────────────────
MODEL_NAME = "nvidia/nemotron-3-super-120b-a12b:free"
FALLBACK_MODEL_NAME = "deepseek/deepseek-chat-v3-0324:free"

# ── Primary LLM ─────────────────────────────────────────────────────────────
llm = ChatOpenRouter(
    model=MODEL_NAME,
    openrouter_api_key=os.getenv("OPEN_ROUTER_API_KEY"),
    temperature=0.7,
    max_tokens=1024,
)

# ── Fallback LLM ─────────────────────────
fallback_llm = ChatOpenRouter(
    model=FALLBACK_MODEL_NAME,
    openrouter_api_key=os.getenv("DEEP_SEEK_API_KEY"),
    temperature=0.7,
    max_tokens=1024,
)
