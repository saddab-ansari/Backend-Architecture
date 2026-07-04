from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'title' : 'Title One', 'author': 'Author One', 'category' : 'Science'},
    {'title' : 'Title Two', 'author': 'Author Two', 'category' : 'Science'},
    {'title' : 'Title Three', 'author': 'Author Three', 'category' : 'History'},
    {'title' : 'Title Four', 'author': 'Author Four', 'category' : 'Maths'},
    {'title' : 'Title Five', 'author': 'Author Five', 'category' : 'Maths'}
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/mybook")
async def read_favorite_book():
    return {'my_book' : 'My favourite Book'}

@app.get("/books/search/")
async def get_book_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return

@app.get("/books/{book_title}")
async def read_book_by_title(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book
    return {"message": "Book not found"}

@app.get("/books/author/{author_name}")
async def all_book_by_author(author_name: str):
    by_author = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            by_author.append(book)
    if len(by_author) > 0:
        return by_author
    else:
        return {'message' : 'No book from this author found.'}

@app.post("/books/create")
async def create_a_book(new_book = Body()):
    BOOKS.append(new_book)
    return new_book

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
