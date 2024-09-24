
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
        <html>
            <body>
                <form action="/upload" enctype="multipart/form-data" method="post">
                    <input name="file" type="file" multiple>
                    <input type="submit">
                </form>
            </body>
        </html>
    """

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print("Received file upload request.")
    try:
        print(f"File details: {file.filename}, {file.content_type}")

        # Read the file contents
        contents = await file.read()
        print("File read successfully.")

        # Attempt to decode the file contents
        try:
            resume_text = contents.decode('utf-8')  # Try utf-8 first
            print(f"Decoded text using utf-8.")
        except UnicodeDecodeError:
            resume_text = contents.decode('latin1')  # Fall back to latin1
            print(f"Decoded text using latin1.")

        print(f"Resume text (first 100 characters): {resume_text[:100]}")  # Print first 100 characters

        return {"filename": file.filename, "content_type": file.content_type}
    except UnicodeDecodeError as e:
        print(f"Error reading file: {e}")
        return {"error": "Failed to decode the file. Please ensure it's in the correct format."}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": str(e)}

