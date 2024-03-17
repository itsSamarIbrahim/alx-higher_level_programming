#!/usr/bin/python3

"""a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""

if __name__ == '__main__':
    import MySQLdb
    import sys

db = MySQLdb.connect(host='localhost',
                     port=3306,
                     user=sys.argv[1],
                     password=sys.argv[2],
                     db=sys.argv[3])

cursor = db.cursor()
state_name = sys.argv[4]
query = "SELECT * FROM states WHERE name LIKE BINARY '{}'
ORDER BY id ASC".format(state_name)
cursor.execute(query)

rows = cursor.fetchall()

for row in rows:
    print(row)

    cursor.close()
    db.close()
