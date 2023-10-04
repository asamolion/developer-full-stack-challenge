from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"
    name = Column(String)
    page_numbers = Column(Integer)
    author_name = Column(String, ForeignKey("authors.name"))

    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"

    name = Column(String, primary_key=True)

    books = relationship("Book", back_populates="author")
