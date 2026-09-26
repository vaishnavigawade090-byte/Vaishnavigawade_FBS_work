# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.


class Book:

    #static variable
    count=0

#constructor:

    def __init__(self, bid=0, bname="", price=0, author=" "):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

        #increase object count
        Book.count= Book.count+1

        def getbid(self):
            return self.bid
        def setbid(self,new_bid):
            self.bid=new_bid

        def getbname(self):
            return self.bname
        def setbname(self,new_bname):
            self.bname=new_bname

        def getprice(self):
            return self.price
        def setprice(self,mew_price):
            self.price=new_price

        def getauthor(self):
            return self.author
        def setauthor(self,new_author):
            self.author=new_author
# Destructor
    def __del__(self):
        print("Book object destroyed")


# ShowBook method
    def ShowBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)

#display
    # def display(self):
    #     print(f"Book ID:{self.bid} ,Book Name:{ self.bname } , Price:{ self.price} ,Author: { self.author}")


# Create object
b1 = Book(101, "Python Programming", 500, "Vaishu")
b1.ShowBook()
print("number of objects created",Book.count)

