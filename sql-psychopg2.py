import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database. A cursor object is another way of
# saying a 'set' or 'list', similar to an 'array' in JavaScript.
# Essentially, anything that we query from the database will become part of
# this cursor object,
# and to read that data, we should iterate over the cursor using a for-loop,
# as an example.
cursor = connection.cursor()

# Query #1 select all records from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist"')

# Query #2 select only the name from the "Artist" table.
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query #3 select Queen from the "Artist" table.
# We need to use a Python string placeholder, (%s) and then define the desired
# string within a list ["Queen"].
# Technically, since we know there should only be one result, we could use the
# .fetchone() method. This would print each column individually, instead of
# part of a tuple of column results.
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# Query #4 select only the "ArtistId"" from the "Artist" table.
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query #5 select only the "Album" from the "ArtistId" 51 from the "Album"
# table.
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query #6 select tracks from the "Track" table where composer is Queen
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# Before we start to query the database, we need to set up a way for our
# data to be retrieved, or fetched, from the cursor.
# fetch the results (multiple)
results = cursor.fetchall()

# to fetch single/particular records from the database
# results = cursor.fetchone()

# Next, once our results have been fetched, we need to end the connection to
#  the database, so the connection isn't always persistent.
connection.close()

# to print results we need to iterate over the results using a for-loop.
for result in results:
    print(result)
