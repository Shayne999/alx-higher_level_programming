#!/usr/bin/python3

"""  lists all cities of that state, using the database """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()

    state_id = sys.argv[4]

    cur.execute("""SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.id = %s""", (state_id,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
