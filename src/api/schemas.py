from pydantic import BaseModel


class User(BaseModel):
    username: str


class UserInDB(User):
    hashed_password: str


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorReturn(AuthorBase):
    id: int


class Author(AuthorBase):
    class Config:
        orm_mode = True


class BookBase(BaseModel):
    name: str
    page_numbers: int


class BookCreate(BookBase):
    author_id: int

    class Config:
        orm_mode = True
