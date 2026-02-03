class product:
    def __init__(self,pid=0,pname='not given',price=0,quantity=0):

        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        

    def getData(self):
        return f'PRODUCT ID:{self.pid}\nPRODUCT NAME:{self.pname}\nPrice:{self.price}\nQUANTITY:{self.quantity}'
    
    

p1 = product(101,'Laptop',5500,3)
print(p1.getData()) 


print("########################################")

p2 = product()
print(p2.getData())