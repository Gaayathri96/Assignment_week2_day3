"""Small LangChain app that sends several prompts to OpenAI via ChatOpenAI.

There is deliberately NO tracing code in this file. LangSmith tracing is
switched on purely through environment variables (see README.md):

    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=LANGSMITH_API_KEY
    LANGSMITH_PROJECT=caie-week2
    OPENAI_API_KEY=OPENAI_API_KEY
"""

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()  # read OPENAI_API_KEY / LANGSMITH_* from .env

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

PROMPTS = [
    "Explain what LangSmith tracing is in two sentences.",
    "Give me three tips for writing clear Python functions.",
    "Write a haiku about debugging code late at night.",
]

for p in PROMPTS:
    print(llm.invoke(p).content)

