# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL


# db = SQL("sqlite:///booksDB-KA_practice.db")
db1 = SQL("sqlite:///moviesDB.db")

db1.execute("CREATE TABLE IF NOT EXISTS movies(name TEXT, release_year NUMBER)")

db1.execute("INSERT INTO movies(name, release_year) VALUES(?, ?)", "The Chosen", 2017)

db1.execute("INSERT INTO movies(name, release_year) VALUES(?, ?)", "Fire Proof", 2008)

db1.execute("INSERT INTO movies(name, release_year) VALUES(?, ?)", "Courageous", 2011)

db1.execute("INSERT INTO movies(name, release_year) VALUES(?, ?)", "Facing the Giants", 2006)

db1.execute("INSERT INTO movies(name, release_year) VALUES(?, ?)", "War Room", 2015)



result = db1.execute("SELECT * FROM movies WHERE release_year > 2012 ORDER BY release_year")

print(result)
