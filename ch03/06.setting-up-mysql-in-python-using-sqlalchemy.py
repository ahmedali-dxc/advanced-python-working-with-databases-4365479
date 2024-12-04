import sqlalchemy

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost:3306/projects', echo=True)