from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True)
    password = Column(String)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    page_numbers = Column(Integer)

    author_id = Column(Integer, ForeignKey("authors.id"))

    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship("Book", back_populates="author")
