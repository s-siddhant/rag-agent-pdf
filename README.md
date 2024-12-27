# RAG Agent for Document Q&A System

This project implements a **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDF documents and ask questions based on their contents. The system uses the **Mistral-7B** language model and **sentence-transformers/all-mpnet-base-v2** embedding model to process documents and respond to queries.

## Technologies Used

- **Python** (version 3.12)
- **FastAPI** for the backend server
- **Streamlit** for the frontend
- **Hugging Face Transformers** for language models and embeddings
- **Docker** for containerization
- **Docker Compose** for orchestrating services

## Project Structure

The project consists of the following components:

- **`rag_pipeline.py`**: The core Python script for processing documents and querying them.
- **`app.py`**: FastAPI backend for file upload and question-answering API.
- **`frontend.py`**: Streamlit frontend for uploading files and asking questions.
- **`docker-compose.yml`**: Docker Compose configuration to run the backend and frontend services.
- **`Dockerfile`**: Dockerfile to containerize the backend service.

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-username/rag-agent-pdf.git
cd rag-agent-pdf
```

1. Create a .env File
Make sure you have your Hugging Face token stored in a .env file (don't push this to your repository for security reasons). Create a .env file in the root directory and add the following:
HF_TOKEN=your_hugging_face_token
