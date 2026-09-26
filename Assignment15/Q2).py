# Q2)Create a class Product with members as pid,pname,price and quantity .Add following methods:
class Product:
    def __init__(self,pid,pname,quantity,price):
        self.pid=pid
        self.pname=pname
        self.quantity=quantity
        self.price=price

        def getpid(self):
            return self.pid
        def setpid(self):
            self.pid=pid

        def getpname(self):
            return self.pname
        def setpname(self):
            self.pname=pname

        def getquantity(self):
            return self.quantity
        def setquantity(self):
            self.quantity=quantity

        def getprice(self):
            return self.price
        def setprice(self):
            self.price=price

#Destructor
    def __del__(self):
        print("Product object destroyed")

#howBook method:
    def ShowBook(self):
            print("Product ID:", self.pid)
            print("Product Name:", self.pname)
            print("Product Price:", self.quantity)
            print("Product Author:", self.price)



#display
#     def display(self):
#         print(f"pid:{self.pid} ,pname {self.pname}, quantity {self.quantity}, price:{self.price}")


# #create object
a1=Product(101,"Sunscreen",12,200)
a1.ShowBook()
        
    