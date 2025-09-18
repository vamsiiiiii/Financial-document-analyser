from celery import Celery
from app.tools import analyze_document
from app.database import save_analysis

celery_app = Celery("worker", broker="redis://localhost:6379/0")

@celery_app.task
def analyze_task(filename: str, content: str):
    result = analyze_document(content)
    save_analysis(filename, result)
    return result
