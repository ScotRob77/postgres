from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# need to link our Python file to our Chinook database, and that's where the
# 'create_engine' component comes into play. I'm going to assign this to a
#  variable of "db" to represent our database, and using create_engine, we can
#  tell it to point to our local Chinook database within our Postgres server.
#  The fact that we have 3 slashes here, signifies that our database is hosted
# locally within our workspace environment.
db = create_engine("postgresql:///chinook")

# The MetaData class will contain a collection of our table objects, and the
# associated data within those objects. Essentially, it's recursive data about
# data, meaning the data about our tables, and the data about the data in those
# tables
meta = MetaData(db)

# create variabe for  "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumID", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)

# Now, we need to actually connect to the database, using the .connect()
# method, and the Python with-statement. This saves our connection to the
# database into a variable called 'connection'.
with db.connect() as connection:

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns(
    # [artist_table.c.Name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(
    # artist_table.c.Name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.ArtistId == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the
    # "Track" table
    select_query = track_table.select().where(
        track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
