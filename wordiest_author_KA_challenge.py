# Source for hands on tutorial that doesn't leave one stuck in a learning loop
# https://www.freecodecamp.org/news/sqlite-python-beginners-tutorial/

from cs50 import SQL


db = SQL("sqlite:///database.db")

db.execute("CREATE TABLE IF NOT EXISTS books(author TEXT, title TEXT, pages INTEGER, publicationyear INTEGER)")

# https://www.amazon.com/Mere-Christianity-C-S-Lewis/dp/0060652926
# https://www.goodreads.com/book/show/11138.Mere_Christianity
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "C.S. Lewis", "Mere Christianity", 227, 1942)

# https://www.amazon.com/Screwtape-Letters-C-S-Lewis/dp/0060652934
# https://www.goodreads.com/book/show/8130077-the-screwtape-letters?ref=nav_sb_ss_1_21
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "C.S. Lewis", "The Screwtape Letters", 160, 1942)

# https://www.amazon.com/Great-Divorce-C-S-Lewis/dp/0060652950
# https://www.goodreads.com/book/show/25845273-the-great-divorce?ref=nav_sb_ss_1_17
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "C.S. Lewis", "The Great Divorce", 160, 1946)

# https://www.goodreads.com/book/show/26077627-a-grief-observed?ref=nav_sb_ss_1_16
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "C.S. Lewis", "A Grief Observed", 76, 1961)

# https://www.goodreads.com/book/show/5907.The_Hobbit?ref=nav_sb_ss_2_30
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "J.R.R. Tolkien", "The Hobbit", 366, 1937)

# https://www.goodreads.com/book/show/61215351-the-fellowship-of-the-ring?ref=nav_sb_ss_1_22
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "J.R.R. Tolkien", "Fellowship of the Ring", 432, 1954)
          
# https://www.goodreads.com/book/show/61215384-the-return-of-the-king?ref=nav_sb_ss_1_18
db.execute("INSERT INTO books (author, title, pages, publicationyear) VALUES(?, ?, ?, ?)", "J.R.R. Tolkien", "Return of the King", 432, 1955)

 

results = db.execute("SELECT author, SUM(pages) AS total_pages FROM books GROUP BY author HAVING total_pages > 1000")

print(results)

  
