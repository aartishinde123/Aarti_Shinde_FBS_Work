#Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class shirt:
    def __init__(self,sid=0,sname='not given',type='',price=0,size=''):

        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        

    def getData(self):
        return f'SHIRT ID:{self.sid}\nSHIRT NAME:{self.sname}\nTYPE:{self.type}\nPrice:{self.price}\nSIZE:{self.size}'
    
    

s1 = shirt(101,'Raymond','Formal',2000,'Small')
print(s1.getData()) 
  

print("########################################")

s2 = shirt()
print(s2.getData())