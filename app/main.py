from fastapi import FastAPI, UploadFile, File
from app.tools import analyze_document
from app.database import save_analysis, init_db
import uvicorn

app = FastAPI(title="Financial Document Analyzer")

# Initialize database
init_db()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()
    analysis = analyze_document(content.decode("utf-8"))
    save_analysis(file.filename, analysis)
    return {"filename": file.filename, "analysis": analysis}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
