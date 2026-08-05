import sqlite3

conn = sqlite3.connect("mineverse.db")
cursor = conn.cursor()

cursor.execute(
    "INSERT INTO players(name, world, status) VALUES (?, ?, ?)",
    ("Steve", "Survival", "online")
)

conn.commit()
conn.close()

print("Player inserted")