#Q3). Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
class Shirt:
    def __init__(self,sid,sname,type,price,size):
        self.sid=sid
        self.sname=sname
        self.type=type
        self.sname=sname
        self.price=price
        self.size=size

        def getsid(self):
            return self.sid
        def setsid(self,new_sid):
            self.sid=new_sid

        def getsname(self):
            return self.sname
        def setsname(self,new_sname):
            self.sname=new_sname

        def gettype(self):
            return self.type
        def settype(self,new_type):
            self.type=new_type

        def getprice(self):
            return self.price
        def setprice(self,new_price):
            self.price=new_price

        def getsize(self):
            return self.size
        def setsize(self,new_size):
            self.size=new_size

#Destructor
    def __del__(self):
        print("Shirt is destroyed")

#showbook:
    def ShowBook(self):
            print("Shirt ID:", self.sid)
            print("Shirt Name:", self.sname)
            print("Shirt Type:", self.type)
            print("Shirt Price:", self.price)
            print("Shirt:",self.size)



    # def display(self):
    #     print(f" sid={self.sid}, sname={self.sname},type={self.type},price={self.price},type={self.type}")

#create object
a1=Shirt(1,"Cotton_shirt","T shirt",400,38)
a1.ShowBook()


