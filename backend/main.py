from fastapi import FastAPI, UploadFile, File
import shutil

app = FastAPI()

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # Call your ML model to get recommendations based on the resume
    return {"recommendations": [{"job": "Example Job 1", "score": 90}, {"job": "Example Job 2", "score": 85}]}

# To run the server, use the command: uvicorn main:app --reload
