import sqlite3

conn = sqlite3.connect("study.db")
cursor = conn.cursor()

def commit():
    conn.commit()
