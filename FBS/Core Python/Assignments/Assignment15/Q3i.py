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
  