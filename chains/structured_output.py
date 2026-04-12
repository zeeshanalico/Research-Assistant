from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

from config import llm
from prompts.constants import structured_prompt

class BookInfo(BaseModel):
    """Structured info about a book."""
    title: str = Field(description="The title of the book")
    author: str = Field(description="The author of the book")
    year: int = Field(description="The year the book was published")
    genre: str = Field(description="The genre of the book")
    summary: str = Field(description="A one-sentence summary of the book")

book_parser = PydanticOutputParser(pydantic_object=BookInfo)

structured_chain = structured_prompt | llm | book_parser


def run_structured_output():
    """Ask the LLM about a book and get back a typed BookInfo object."""
    print("\n  Structured Output Demo")
    print("  Ask about any book and get back a typed Python object.\n")

    query = input("Enter a book name (e.g. '1984'): ").strip()
    if not query:
        return

    try:
        chain_with_instructions = (
            structured_prompt.partial(
                format_instructions=book_parser.get_format_instructions()
            )
            | llm
            | book_parser
        )

        result: BookInfo = chain_with_instructions.invoke({"query": query})

        print(f"\n  Parsed BookInfo object:")
        print(f"    title   : {result.title}")
        print(f"    author  : {result.author}")
        print(f"    year    : {result.year}")
        print(f"    genre   : {result.genre}")
        print(f"    summary : {result.summary}")
        print(f"\n  Type: {type(result).__name__}\n")
    except Exception as e:
        print(f"Error: {e}\n")
