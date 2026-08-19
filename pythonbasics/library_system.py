class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id:str, title:str, author:str):
        self.books[book_id] = {
            "title": title,
            "author": author,
            "availability": True
        }

    def borrow_book(self, book_id:str):
        if self.books[book_id]["availability"] == True:
            self.books[book_id]["availability"] = False

    def return_book(self, book_id:str):
        if self.books[book_id]["availability"] == False:
            self.books[book_id]["availability"] = True

    def remove_book(self, book_id:str):
        self.books.pop(book_id, None)

    def lookup_book(self, book_id:str) -> str:
        return self.books[book_id]

    def list_all_books(self):
        return "\n".join(
            f"Book ID: {book_id} Book Title: {details['title']} Book Author: {details['author']} Availability: {details['availability']}"
            for book_id, details in self.books.items()
        )

books = Library()

books.add_book("THE060", "Christian Beliefs", "John Wesley")
books.add_book("PHY506", "Physics Theorems", "Isaac Newton")
books.add_book("ELE400", "Electronics Fundamentals", "Vincent Volts")

books.borrow_book("THE060")

books.remove_book("PHY506")

print(books.lookup_book("ELE400"))
print(books.list_all_books())