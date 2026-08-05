import sqlite3

conn = sqlite3.connect("mineverse.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    world TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")