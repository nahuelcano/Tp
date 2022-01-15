from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Registro.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()