import fitz

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_core.documents import Document

from langchain_community.vectorstores import Chroma

from embeddings import get_embedding_model

CHROMA_PATH = "../chroma_db"

embedding_model = get_embedding_model()


def extract_text_from_pdf(pdf_path):

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:

        text += page.get_text()

    return text


def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=1000,

        chunk_overlap=200
    )

    chunks = splitter.split_text(text)

    return chunks


def store_in_vector_db(chunks):

    documents = [

        Document(page_content=chunk)

        for chunk in chunks
    ]

    vectorstore = Chroma.from_documents(

        documents=documents,

        embedding=embedding_model,

        persist_directory=CHROMA_PATH
    )

    vectorstore.persist()

    return len(documents)