class Shirt:
    # Static size increment %
    size_price = {"small": 0, "medium": 10, "large": 20, "xlarge": 30}

    # Constructor (parameterized + parameterless)
    def __init__(self, sid=None, sname=None, stype=None, price=0, size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    # Destructor
    def __del__(self):
        print("Shirt object destroyed")

    # Method to calculate final price
    def finalPrice(self):
        inc = Shirt.size_price.get(self.size, 0)
        return self.price + (self.price * inc / 100)

    # Show method
    def ShowShirt(self):
        print("ID:", self.sid)
        print("Name:", self.sname)
        print("Type:", self.stype)
        print("Size:", self.size)
        print("Final Price:", self.finalPrice())


# Testing
s = Shirt(1, "Classic", "Formal", 1000, "large")
s.ShowShirt()
