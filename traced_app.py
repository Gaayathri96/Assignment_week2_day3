"""Small LangChain app that sends several prompts to OpenAI via ChatOpenAI.

There is deliberately NO tracing code in this file. LangSmith tracing is
switched on purely through environment variables (see README.md):

    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=<your LangSmith key>
    LANGSMITH_PROJECT=week2-day3-traced-app
    OPENAI_API_KEY=<your OpenAI key>
"""

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

PROMPTS = [
    "Explain what LangSmith tracing is in two sentences.",
    "Give me three tips for writing clear Python functions.",
    "Write a haiku about debugging code late at night.",
]


def main() -> None:
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a concise, helpful assistant."),
            ("human", "{question}"),
        ]
    )
    chain = prompt | llm | StrOutputParser()

    for i, question in enumerate(PROMPTS, start=1):
        answer = chain.invoke({"question": question})
        print(f"--- Prompt {i} ---")
        print(f"Q: {question}")
        print(f"A: {answer}\n")


if __name__ == "__main__":
    main()
