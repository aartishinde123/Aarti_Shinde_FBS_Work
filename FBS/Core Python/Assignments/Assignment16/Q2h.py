class Product:
    
    discount = 10   

    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    @staticmethod
    def showDiscount():
        print("Current Discount:", Product.discount, "%")



p1 = Product(1, "Mobile", 20000, 5)
Product.showDiscount()
