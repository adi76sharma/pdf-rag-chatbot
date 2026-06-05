import os

from dotenv import load_dotenv

from groq import Groq

from langchain_community.vectorstores import Chroma

from embeddings import get_embedding_model

load_dotenv()

# Render-friendly path
CHROMA_PATH = "chroma_db"

embedding_model = get_embedding_model()

vectorstore = Chroma(
    persist_directory=CHROMA_PATH,
    embedding_function=embedding_model
)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_question(query):

    docs = vectorstore.similarity_search(
        query,
        k=3
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a helpful PDF assistant.

Answer ONLY using the provided context.

If answer is not in context,
say:
"I could not find this in the PDF."

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
