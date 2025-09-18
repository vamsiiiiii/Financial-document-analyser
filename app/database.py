import sqlite3

DB_NAME = "analysis.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            analysis TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_analysis(filename: str, analysis: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO analyses (filename, analysis) VALUES (?, ?)", (filename, analysis))
    conn.commit()
    conn.close()
