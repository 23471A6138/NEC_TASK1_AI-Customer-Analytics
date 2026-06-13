import sqlite3

conn = sqlite3.connect("database/customers.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS prediction_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    age INTEGER,
    income INTEGER,
    score INTEGER,
    prediction TEXT
)
""")

conn.commit()
conn.close()

print("Table Created Successfully")