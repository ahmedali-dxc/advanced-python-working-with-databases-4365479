from sqlalchemy import Table, Column, Integer, Float, String, MetaData, create_engine

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/red30', echo=True)

metadata = MetaData()

sales_table = Table('sales', metadata, autoload_with=engine)

metadata.create_all(engine)