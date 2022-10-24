class Book:
    def __init__(self, title, author, price, quantity) -> None:
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity

book1 = Book('Python', 'Corey Schefer', 300, 20)
book2 = Book('Machine Learning', 'Matt Harrison', 200, 15)
book3 = Book('Physics', 'HC Verma', 400, 50)

print(book1)
print(book2)
print(book3)
