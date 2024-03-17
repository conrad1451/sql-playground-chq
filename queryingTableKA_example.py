# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL


# db = SQL("sqlite:///booksDB-KA_practice.db")
db1 = SQL("sqlite:///groceriesDB.db")

db1.execute("CREATE TABLE IF NOT EXISTS groceries(name TEXT, quantity NUMBER, aisle STRING)")

db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "bananas", 4, 7)
db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "Peanut Butter", 1, 2)
db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "Dark Chocolate Bars", 2, 2)
db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "Ice cream", 1, 12)
db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "Cheeries", 6, 2)
db1.execute("INSERT INTO groceries(name, quantity, aisle) VALUES(?, ?, ?)", "Chocolate syrup", 1, 4)

result = db1.execute("SELECT * FROM groceries WHERE aisle > 5 ORDER BY aisle")

print(result)
