import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("""
SELECT AVG(age)
FROM people
""")

result = cursor.fetchone()

print("平均年齢：",result[0])

conn.close()