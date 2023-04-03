#!/usr/bin/python3
import MySQLdb

# Create the database
db = MySQLdb.connect(host="localhost", user="oduor", password="unL3A2ht00r22!", db="test_db")
if (db):
    print("Database connected successfully")
else:
    print("Connection to Database failed")

# Prepare a cursor object
cursor = db.cursor()
if (cursor):
    print("Created Cursor successfully")
else:
    print("Failed to Create Cursor: Press (1) to retry, (0) to quit")

# Execute Commands
## TABLE CREATION
cursor.execute("CREATE TABLE IF NOT EXISTS song (id INT PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL)")

## INSERT
songs = ("Anaconda", "Mafia", "Foxy Lady")
for song in songs:
    cursor.execute("INSERT INTO song (title) VALUES (%s)", (song,))
    print("Auto Increment ID:",cursor.lastrowid)

## Multiple Substitution Query
cursor.execute("SELECT * FROM song WHERE id = %s or id = %s", (1,2))

## Execute Select
numrows = cursor.execute("SELECT * FROM song")
print("Selected %s rows" % numrows)
print("Selected %s rows" % cursor.rowcount)

# OBTAINING QUERY RESULTS

## Fetch all at once 
cursor.execute("SELECT * FROM song")
rows = cursor.fetchall()
for row in rows:
    for col in row:
        print("%s," % col)
    print("\n")

## Fetch one at a time
cursor.execute("SELECT * FROM song WHERE id = 1")
print("Id: %s -- Title: %s" % (cursor.fetchone()))

# HANDLING EXCEPTIONS

## Exceptions and errors

# --> Get data from db
try:
    cursor.execute("SELECT * FROM song")
    rows = cursor.fetchall()
except MySQLdb.Error as e:
    try:
        print("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
    except IndexError:
            print("MySQL Error: %s" % str(e))
    # Print results in comma delimited format
    for row in rows:
        for col in row:
            print("%s," % col)
        print("\n")

# CLEAN UP
cursor.close()
db.close()