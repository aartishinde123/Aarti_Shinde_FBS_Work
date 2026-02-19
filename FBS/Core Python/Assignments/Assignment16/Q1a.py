#Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book:
    def __init__(self,book_id=0,book_name='',price=0,author=''):

        self.book_id = book_id
        self.book_name = book_name
        self.price = price
        self.author = author
        

    def getData(self):
        return f'BOOK ID:{self.book_id}\nBOOK NAME:{self.book_name}\nPrice:{self.price}\nAuthor:{self.author}'
    
    

b1 = Book(101,'Rich Dad Poor Dad',500,'Robert T')
print(b1.getData()) 
 

print("########################################")

b2 = Book()
print(b2.getData())