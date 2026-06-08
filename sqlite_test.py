import sqlite3

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("""
SELECT AVG(age)
FROM people
""")

result = cursor.fetchone()

average_age = result[0]

print("平均年齢：",average_age)

if average_age >= 30:
    print("平均年齢は３０歳以上です。")

else:
    print("平均年齢は３０歳未満です。")

conn.close()