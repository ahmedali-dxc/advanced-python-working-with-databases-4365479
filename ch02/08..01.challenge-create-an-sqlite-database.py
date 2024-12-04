import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Users (user_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, email_address TEXT)")

users = [
  ('Ahmed', 'Ali', 'aaliibrahime@dxc.com'),
  ('Rana', 'Mohamed', 'rana.mohamed2@dxc.com'),
  ('Ghada', 'Gamal', 'ghada.gam.abd-el-hafez@dxc.com'),
  ('Ahmed', 'Ali', 'ahmed.ali.emam@gmail.com'),
  ('Gamer', 'Ali', 'gamer.ahmed.alii@gmail.com')
]

cursor.executemany("INSERT INTO Users (first_name, last_name, email_address) VALUES (?, ?, ?)", users)
cursor.execute("SELECT * FROM Users")

print(cursor.fetchall())

connection.commit()
connection.close()