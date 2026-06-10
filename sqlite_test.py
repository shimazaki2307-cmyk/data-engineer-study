import sqlite3

def get_average_age():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    cursor.execute("SELECT AVG(age) FROM people")

    result = cursor.fetchone()[0]

    conn.close()

    return result

def get_count():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM people")

    result = cursor.fetchone()[0]

    conn.close()

    return result

print("人数：",get_count())
print("平均年齢：",get_average_age())