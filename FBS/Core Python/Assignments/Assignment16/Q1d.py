class Book:
    # Static variable
    count = 0

    # Constructor (supports parameterized and parameterless)
    def __init__(self, bid=None, bname=None, price=0.0, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        
        Book.count += 1   # Increase count when object is created
        print("Book object created")

    # Destructor
    def __del__(self):
        Book.count -= 1   # Decrease count when object is deleted
        print("Book object destroyed")

    # ShowBook method
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

    # Static method to show count
    @staticmethod
    def showCount():
        print("Total Book objects:", Book.count)


# ---- Testing ----

# Parameterless constructor
b1 = Book()

# Parameterized constructor
b2 = Book(101, "Python Basics", 450.0, "John Doe")

b2.ShowBook()

Book.showCount()
