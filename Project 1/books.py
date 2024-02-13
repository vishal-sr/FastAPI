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


@app.get("/books/")
async def get_all_books():
    return {"books": bks}


@app.get("/book/{author}")
async def get_book_by_author(author: str):
    bs = [book for book in bks if book["author"] == author]
    return {"books": bs}


@app.get("/book/")
async def get_book_by_rating_gt(rating: int):
    bs = [book for book in bks if book["rating"] > rating]
    return {"books": bs}


@app.post("/books/")
async def create_new_book(newBook: dict = Body()):
    bks.append(newBook)
    return {"message": "New book added to books"}


@app.put("/book/")
async def update_book(dataToUpdate: dict = Body()):
    for i in range(len(bks)):
        if bks[i]["title"].casefold() == dataToUpdate["title"].casefold():
            bks[i] = dataToUpdate
            print(bks)
            return {"message": "Successfully updated!!!"}


@app.delete("/book/{bookTitle}")
async def update_book(bookTitle: str):
    for i in range(len(bks)):
        if bks[i]["title"].casefold() == bookTitle.casefold():
            bks.pop(i)
            return {"message": "Successfully deleted!!!"}
