class product:
    def __init__(self,pid,pname,price,quantity):

        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        

    def showData(self):
        return f'PRODUCT ID:{self.pid}\nPRODUCT NAME:{self.pname}\nPrice:{self.price}\nQUANTITY:{self.quantity}'
    
    

p1 = product(101,'Laptop',5500,3)
print(p1.showData()) 
 