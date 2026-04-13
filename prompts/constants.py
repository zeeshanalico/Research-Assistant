from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

RESEARCH_SYSTEM = (
    "You are a research assistant. Given a topic, list 4 key bullet points. "
    "Be concise and factual."
)

SUMMARY_SYSTEM = (
    "Summarize the following key points into a short 2-3 sentence paragraph."
)

QUIZ_SYSTEM = (
    "Based on the following key points, create 3 short quiz questions with answers."
)

CHAT_SYSTEM = (
    "You are a helpful AI tutor. Answer questions clearly and remember "
    "the conversation context."
)

STRUCTURED_SYSTEM = (
    "You are a helpful assistant. Extract the requested information "
    "and respond ONLY with valid JSON matching the given format.\n\n"
    "{format_instructions}"
)

STREAMING_SYSTEM = (
    "You are a creative storyteller. Write a short, engaging story "
    "about the given topic in 3-4 paragraphs."
)

FALLBACK_SYSTEM = (
    "You are a helpful assistant. Answer the user's question concisely."
)

TOOLS_SYSTEM = (
    "You are a helpful assistant with access to tools. "
    "Always use tools for mathematical operations."
)


# ────────────────────────────────────────────────────────────────────────────
# PROMPT TEMPLATES (ready-to-use in chains)
# ────────────────────────────────────────────────────────────────────────────

key_points_prompt = ChatPromptTemplate.from_messages([
    ("system", RESEARCH_SYSTEM),
    ("human", "Topic: {topic}"),
])

summary_prompt = ChatPromptTemplate.from_messages([
    ("system", SUMMARY_SYSTEM),
    ("human", "{key_points}"),
])

quiz_prompt = ChatPromptTemplate.from_messages([
    ("system", QUIZ_SYSTEM),
    ("human", "{key_points}"),
])

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", CHAT_SYSTEM),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

structured_prompt = ChatPromptTemplate.from_messages([
    ("system", STRUCTURED_SYSTEM),
    ("human", "{query}"),
])

streaming_prompt = ChatPromptTemplate.from_messages([
    ("system", STREAMING_SYSTEM),
    ("human", "Write a short story about: {topic}"),
])

fallback_prompt = ChatPromptTemplate.from_messages([
    ("system", FALLBACK_SYSTEM),
    ("human", "{input}"),
])
