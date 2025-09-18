# 📊 Financial Document Analyzer (Debug Challenge)

## ✅ Overview
This project is a **financial document analyzer system** built with **FastAPI** and debugged for the AI Internship Assignment.  
It supports file uploads, extracts financial insights, and stores results in a database.

---

## 🐛 Bugs Found & Fixes

Bug 1: API returning {"detail":"Not Found"}
🔧 Fixed FastAPI route registration (app.include_router).

Bug 2: Incorrect file handling (PDFs failing)
🔧 Used pdfplumber consistently and validated file MIME type.

Bug 3: Inefficient prompts
🔧 Rewrote prompts for concise context-specific answers.

Bug 4: Blocking requests under load
🔧 Added Celery + Redis worker for async task handling.

---

## 🚀 Setup

### 1. Clone & Install
```bash
git clone https://github.com/your-username/financial-document-analyzer.git
cd financial-document-analyzer
pip install -r requirements.txt
```

### 2. Run API
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. Access
- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check → [http://localhost:8000/health](http://localhost:8000/health)

---

## 📂 API Endpoints

| Method | Endpoint  | Description |
|--------|-----------|-------------|
| GET    | `/health` | Check if server is alive |
| POST   | `/analyze`| Upload a document and get analysis |

Example Response:
```json
{
  "filename": "report.pdf",
  "analysis": "Mentions revenue figures. Mentions growth or percentages."
}
```

---

## ⚡ Bonus Features
- **Queue Worker (Celery + Redis):** Process heavy documents asynchronously.
- **Database (SQLite):** Store uploaded docs + analyses.

---

## 🎯 Submission Requirements Covered
- ✅ Fixed bugs
- ✅ Efficient prompts
- ✅ Working code
- ✅ README with docs & setup
- ✅ Bonus: Queue Worker + DB
