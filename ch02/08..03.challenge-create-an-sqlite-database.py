import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///users.db", echo=True)

users = [
  {'first_name': 'Heba', 'last_name': 'Abd El-Rahman', 'email_address': 'heba.abd-el-rahman-ahmed-abd-el-rah@dxc.com'},
  {'first_name': 'Ehab', 'last_name': 'Emara', 'email_address': 'ehab.emara@dxc.com'}
]

metadata = sqlalchemy.MetaData()

users_table = sqlalchemy.Table("users",
                               metadata,
                               sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
                               sqlalchemy.Column("first_name", sqlalchemy.String),
                               sqlalchemy.Column("last_name", sqlalchemy.String),
                               sqlalchemy.Column("email_address", sqlalchemy.String))

metadata.create_all(engine)

with engine.connect() as conn:
  conn.execute(sqlalchemy.insert(users_table).values(users))
  for row in conn.execute(sqlalchemy.select(users_table)):
    print(row)
  conn.commit()