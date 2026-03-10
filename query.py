from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


def main():
    load_dotenv()

    embeddings = OpenAIEmbeddings()

    vectorstore = Chroma(
        persist_directory="vectorstore",
        embedding_function=embeddings
    )

    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    while True:
        question = input("\nQuestion: ")

        if question.lower() in ["exit", "quit"]:
            break

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

        print("\nAnswer:")
        print(response.content)


if __name__ == "__main__":
    main()