import streamlit as st
import requests

# Streamlit app title
st.title("Document Q&A System")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

# Handle file upload
if uploaded_file:
    st.success("File uploaded successfully!")
    # Save the file locally
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.info("File saved locally. Ready to process!")

    # Upload file to backend
    if st.button("Upload to Backend"):
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        #response = requests.post("http://127.0.0.1:8000/upload", files=files) #works on local
        response = requests.post("http://backend:8000/upload", files=files) #changed for docker
        if response.status_code == 200:
            st.success("File successfully uploaded to backend!")
        else:
            st.error("Failed to upload file to backend.")

# Ask questions
question = st.text_input("Ask a question about the document:")
if question:
    if st.button("Get Answer"):
        #response = requests.post("http://127.0.0.1:8000/ask", json={"question": question}) #works on local
        response = requests.post("http://backend:8000/ask", json={"question": question}) #changed for docker
        if response.status_code == 200:
            st.write("**Answer:**", response.json().get("answer"))
        else:
            st.error("Failed to get an answer.")
