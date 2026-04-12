Research Assistant
==================

A menu-driven app where each option demonstrates different LangChain concepts.

### Concepts covered across the project:

1. ChatPromptTemplate        — structured prompt building          (prompts/constants.py)
2. MessagesPlaceholder       — inject chat history into prompts    (prompts/constants.py)
3. StrOutputParser           — AIMessage → plain string            (chains/research.py)
4. PydanticOutputParser      — AIMessage → typed Python object     (chains/structured_output.py)
5. Sequential Chains (|)     — pipe one chain's output to the next (chains/research.py)
6. RunnablePassthrough.assign— keep keys + add new ones in a chain (chains/research.py)
7. RunnableParallel          — run multiple chains simultaneously  (chains/research.py)
8. RunnableLambda            — plug any Python function into chain  (utils/formatters.py)
9. Conversation Memory       — multi-turn chat with history        (chains/chat.py)
10. Batch Processing (.batch) — process multiple inputs at once     (chains/batch.py)
11. Streaming (.stream)       — token-by-token output               (chains/streaming.py)
12. Fallbacks (.with_fallbacks) — auto-retry with a backup model    (chains/fallback.py)
13. InMemoryCache             — cache identical LLM calls           (config.py)

### Run:

```
pip install -r requirements.txt

python main.py
```
