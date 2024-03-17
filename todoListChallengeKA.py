# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL

db1 = SQL("sqlite:///todolistDB.db")

db1.execute("CREATE TABLE IF NOT EXISTS todo_list(item TEXT, minutes NUMBER)")

db1.execute("INSERT INTO todo_list(item, minutes) VALUES(?, ?)", "Wash the dishes", 15)

db1.execute("INSERT INTO todo_list(item, minutes) VALUES(?, ?)", "Vacuuming", 20)

db1.execute("INSERT INTO todo_list(item, minutes) VALUES(?, ?)", "Learn some stuff on KA", 30)

db1.execute("INSERT INTO todo_list(item, minutes) VALUES(?, ?)", "Cook food", 40)

result = db1.execute("SELECT SUM(minutes) FROM todo_list")
print(result)
