from fastapi import FastAPI, UploadFile, File

import os

from ingest import (
    extract_text_from_pdf,
    chunk_text,
    store_in_vector_db
)

from query import ask_question

app = FastAPI()

UPLOAD_FOLDER = "../uploads"

@app.get("/")
def home():

    return {
        "message": "PDF RAG Running"
    }

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as f:

        f.write(await file.read())

    text = extract_text_from_pdf(file_path)

    chunks = chunk_text(text)

    total_chunks = store_in_vector_db(chunks)

    return {

        "filename": file.filename,

        "total_chunks": total_chunks,

        "message": "PDF processed successfully"
    }

@app.get("/ask")
def ask(query: str):

    answer = ask_question(query)

    return {

        "question": query,

        "answer": answer
    }