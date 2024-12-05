from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/red30', echo=True)

Base = automap_base()

Base.prepare(autoload_with=engine)

Sales = Base.classes.sales