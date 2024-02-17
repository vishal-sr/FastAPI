from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int


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


@app.post("/create-book")
async def create_book(book: Book):
    book = Book(**book.model_dump())
    books.append(book)
