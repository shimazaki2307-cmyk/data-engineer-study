import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

for row in cursor.execute("""
SELECT COUNT(*)
FROM people
WHERE age >= 30
"""):
    print(row)

conn.close()