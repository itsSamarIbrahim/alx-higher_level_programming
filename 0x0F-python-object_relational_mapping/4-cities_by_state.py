#!/usr/bin/python3

"""a script that lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("""
    SELECT cities.id, cities.name, states.name
    FROM cities LEFT JOIN states ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """)

    rows = cursor.fetchall()
    for row in rows:
        print(row)
