from sqlalchemy import column, Integer, String  # , ForeignKey
from config import Base


class Book(Base):
    __tablename__ = "book"
    id = column(Integer, primary_key=True)
    title = column(String)
    description = column(String)
