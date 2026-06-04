import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

for row in cursor.execute("""
SELECT *
FROM people
WHERE age >= 25
"""):
    print(row)

conn.close()