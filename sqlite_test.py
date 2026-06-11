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