from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=25)
    author: str = Field(min_length=1, max_length=25)
    description: str = Field(min_length=1, max_length=250)
    rating: int = Field(gt=0, lt=6)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "New book",
                "author": "New Author",
                "description": "New book's description",
                "rating": 3
            }
        }


books = [
    Book(id=1, title="Book 1", author="Author 1",
         description="Description 1", rating=5),
    Book(id=2, title="Book 2", author="Author 2",
         description="Description 2", rating=4),
    Book(id=3, title="Book 3", author="Author 3",
         description="Description 3", rating=3),
    Book(id=4, title="Book 4", author="Author 4",
         description="Description 4", rating=2),
    Book(id=5, title="Book 5", author="Author 5",
         description="Description 5", rating=1),
    Book(id=6, title="Book 6", author="Author 6",
         description="Description 6", rating=5),
    Book(id=7, title="Book 7", author="Author 7",
         description="Description 7", rating=4),
    Book(id=8, title="Book 8", author="Author 8",
         description="Description 8", rating=3),
    Book(id=9, title="Book 9", author="Author 9",
         description="Description 9", rating=2),
    Book(id=10, title="Book 10", author="Author 10",
         description="Description 10", rating=1)
]


@app.get("/")
async def get_all_books():
    return books


@app.post("/create-book/")
async def create_book(book: Book):
    book = Book(**book.model_dump())
    book.id = next_book_id()
    books.append(book)


@app.get("/book/{bookID}/")
async def get_book_by_id(bookID: int) -> Book:
    for book in books:
        if book.id == bookID:
            return book


@app.get("/books/")
async def filter_books_by_rating(rating: int) -> list[Book]:
    return [book for book in books if book.rating == rating]


@app.put("/book/update-book/")
async def update_book(book: Book):
    for i, bk in enumerate(books):
        if bk.id == book.id:
            books[i] = book


@app.delete("/book/delete")
async def delete_book_by_id(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            books.pop(i)
            break


def next_book_id() -> int: return books[-1].id + 1 if len(books) > 0 else 1
