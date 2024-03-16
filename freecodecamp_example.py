# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL


db = SQL("sqlite:///database.db")

db.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, age NUMBER, fav_food STRING)")

db.execute("INSERT INTO users(name, age, fav_food) VALUES(?, ?, ?)", "eesa", 14, "pizza")

db.execute("INSERT INTO users(name, age, fav_food) VALUES(?, ?, ?)", "Conrad", 24, "jollof rice")


def print_db_contents(my_db):
  print("In the current database, the entries are:")
  print()
  for user_entry in my_db:
    print(user_entry)

people = db.execute("SELECT * FROM users")
print_db_contents(people)

people_fav_foods = db.execute("SELECT DISTINCT age, fav_food FROM users")

# people_fav_foods = db.execute("SELECT DISTINCT fav_food FROM users")
print(people_fav_foods)


people2 = db.execute("SELECT * FROM users WHERE name='Conrad' AND age=24")
print("\n")
print(people2)

print("\n")
print("\n")
print("\n")

db.execute("UPDATE users SET fav_food='shawarma' WHERE name='Conrad'")

people3 = db.execute("SELECT * FROM users WHERE name='Conrad' AND age=24")
print("\n")
print(people3)


print("\n\n\nNow we remove a user from the database:\n")
db.execute("DELETE FROM users WHERE name='Conrad'")

people = db.execute("SELECT * FROM users")
print_db_contents(people)
