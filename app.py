from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from rag_pipeline import process_document, query_document
import os

app = FastAPI()

# Store the index temporarily
index = None

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global index
    try:
        # Save the uploaded file
        file_path = f"temp_{file.filename}"
        with open(file_path, "wb") as f:
            f.write(await file.read())

        # Process the document
        index = process_document(file_path)

        # Delete the file after processing
        os.remove(file_path)
        return {"message": f"Successfully processed {file.filename}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    global index
    if not index:
        raise HTTPException(status_code=400, detail="No document uploaded yet. Please upload a document first.")
    try:
        answer = query_document(index, request.question)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "Welcome to the RAG API! Upload a document to start querying."}
