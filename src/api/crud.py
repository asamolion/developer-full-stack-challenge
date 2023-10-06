"""
All CRUD utilities are defined in this module
"""
from sqlalchemy.orm import Session

import models
import schemas


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        name=book.name,
        page_numbers=book.page_numbers,
        author_id=book.author_id,
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books_by_author(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id == author_id)


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_author(db: Session, author: schemas.AuthorIn):
    db_author = models.Author(name=author.name)

    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(models.Author.id == author_id).first()
