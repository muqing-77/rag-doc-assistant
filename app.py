import streamlit as st
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma


load_dotenv()

st.set_page_config(page_title="RAG Document Assistant", page_icon="📄")
st.title("📄 RAG Document Assistant")
st.write("Ask questions based on the documents stored in the local vector database.")

# 初始化模型和向量库
@st.cache_resource
def load_rag_components():
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

    return retriever, llm


retriever, llm = load_rag_components()

# 用户输入
question = st.text_input("Enter your question:")

if question:
    with st.spinner("Retrieving relevant context and generating answer..."):
        docs = retriever.invoke(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Use the following context to answer the question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}
"""

        response = llm.invoke(prompt)

    st.subheader("Answer")
    st.write(response.content)

    with st.expander("Retrieved Context"):
        for i, doc in enumerate(docs, 1):
            st.markdown(f"**Chunk {i}:**")
            st.write(doc.page_content)