class Product:
    discount = 10   # 10% discount

    def __init__(self, pid, pname, price, quantity):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def applyDiscount(self):
        discount_amount = self.price * Product.discount / 100
        self.price -= discount_amount

    def showProduct(self):
        print("ID:", self.pid)
        print("Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


# ---- Testing ----
p1 = Product(2, "Laptop", 50000, 2)

print("Before Discount:")
p1.showProduct()

p1.applyDiscount()

print("\nAfter Discount:")
p1.showProduct()
