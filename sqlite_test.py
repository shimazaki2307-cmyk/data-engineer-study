import sqlite3

def get_people():
    conn = sqlite3.connect ("sample.db")
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT name,age
                   FROM people
                   """)
    
    result = cursor.fetchall()
    
    conn.close()
    
    return result

people = get_people()

for person in people:
    print(person)

def get_people_over_30():
    conn = sqlite3.connect("sample.db")
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT name,age
                   FROM people
                   WHERE age >= 30
                   """)
    
    result = cursor.fetchall()

    conn.close()

    return result

people = get_people_over_30()

for person in people:
    print("名前：",person[0],"年齢：",person[1])