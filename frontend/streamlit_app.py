import streamlit as st

import requests

BACKEND_URL = "http://127.0.0.1:8000"

st.title("PDF RAG Chatbot")

uploaded_file = st.file_uploader(

    "Upload PDF",

    type="pdf"
)

if uploaded_file:

    files = {

        "file": uploaded_file
    }

    response = requests.post(

        f"{BACKEND_URL}/upload",

        files=files
    )

    st.success(

        response.json()["message"]
    )

question = st.text_input(

    "Ask question from PDF"
)

if st.button("Ask"):

    response = requests.get(

        f"{BACKEND_URL}/ask",

        params={
            "query": question
        }
    )

    answer = response.json()["answer"]

    st.write(answer)