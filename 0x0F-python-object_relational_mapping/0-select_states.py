#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

def list_status(username, password, database):
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db=database)
    cur = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close the db connection
    db.close()

    # Usage

    if __name__ == '__main__':
        username = sys.argv[1]
        username = sys.argv[2]
        username = sys.argv[3]

        list_status(username, password. database)
