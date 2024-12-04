import sqlite3

# open/create a database connection
connection = sqlite3.connect("movies.db")

# cursor to execute commands
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies (Title TEXT, Director TEXT, Year INT)''')

# commit and close
connection.commit()
connection.close()