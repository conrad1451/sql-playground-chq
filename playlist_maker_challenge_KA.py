# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL


db = SQL("sqlite:///database.db")

db.execute("CREATE TABLE IF NOT EXISTS artists(name TEXT, country TEXT, genre TEXT)")

db.execute("INSERT INTO artists (name, country, genre) VALUES(?, ?, ?)", "Swoope", "US", "CHH")
db.execute("INSERT INTO artists (name, country, genre) VALUES(?, ?, ?)", "KB", "US", "CHH")
db.execute("INSERT INTO artists (name, country, genre) VALUES(?, ?, ?)", "Tedashii", "US", "CHH")
db.execute("INSERT INTO artists (name, country, genre) VALUES(?, ?, ?)", "Trip Lee", "US", "CHH")

db.execute("CREATE TABLE IF NOT EXISTS songs(artist TEXT, title TEXT)")

db.execute("INSERT INTO songs(artist, title) VALUES(?, ?)", "Tedashii", "God Flex")

db.execute("INSERT INTO songs(artist, title) VALUES(?, ?)", "Swoope", "Everybody's Going Through")

db.execute("INSERT INTO songs(artist, title) VALUES(?, ?)", "KB", "Armies")
db.execute("INSERT INTO songs(artist, title) VALUES(?, ?)", "KB", "Too God")
db.execute("INSERT INTO songs(artist, title) VALUES(?, ?)", "KB", "Danza")

song_titles = db.execute("SELECT title FROM songs")
chh_artists = db.execute("SELECT name FROM artists WHERE genre = 'CHH'")
kb_songs = db.execute("SELECT title FROM songs WHERE artist = 'KB'")

print(song_titles)
print("")
print(chh_artists)
print("")
print(kb_songs)
