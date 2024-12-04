import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///users.db", echo=True)

users = [
  {'first_name': 'Heba', 'last_name': 'Kamal', 'email_address': 'hebatallah.kam.el-deen-ramadan@dxc.com'},
  {'first_name': 'Ahmed', 'last_name': 'Azzam', 'email_address': 'ahmed.azzam@gmail.com'},
  {'first_name': 'Ognyan', 'last_name': 'Georgiev', 'email_address': 'ognyan.georgiev@dxc.com'},
  {'first_name': 'Mohamed', 'last_name': 'Sobhy', 'email_address': 'm.sobhy@dxc.com'},
  {'first_name': 'Hazem', 'last_name': 'Khalil', 'email_address': 'hazem.khalil@gmail.com'}
]

with engine.connect() as conn:
  conn.execute(sqlalchemy.text('''
                               CREATE TABLE IF NOT EXISTS Users (user_id integer primary key autoincrement,
                               first_name text,
                               last_name text,
                               email_address text)
                               '''))
  conn.execute(sqlalchemy.text('''
                               INSERT INTO Users (first_name, last_name, email_address) 
                               VALUES (:first_name, :last_name, :email_address)
                               '''), users)
  result = conn.execute(sqlalchemy.text("SELECT * FROM Users"))
  for row in result:
    print(row)

  conn.commit()