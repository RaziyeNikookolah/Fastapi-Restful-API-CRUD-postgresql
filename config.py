from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:postgres@localhost.5432/python_db"
engin = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engin)
base = declarative_base()
