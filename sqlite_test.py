import sqlite3

def get_average_age():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT AVG(age)
    FROM people
    """)

    result = cursor.fetchone()[0]

    conn.close()

    return result

average_age = get_average_age()

print("平均年齢：",average_age)