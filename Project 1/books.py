from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


bks = [
    {"title": "my book", "author": "vishal", "rating": 3},
    {"title": "my book 2", "author": "vishal", "rating": 5},
    {"title": "random book", "author": "random", "rating": 1},
]


@app.get("/")
async def first_api():
    return {"message": "Hello Vishal!"}


@app.get("/book/{author}")
async def get_book_by_author(author: str):
    bs = [book for book in bks if book["author"] == author]
    return {"books": bs}


@app.get("/book/")
async def get_book_by_rating_gt(rating: int):
    bs = [book for book in bks if book["rating"] > rating]
    return {"books": bs}
