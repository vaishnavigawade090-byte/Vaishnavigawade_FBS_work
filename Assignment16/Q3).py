# Q3). Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. For each size of shirt price should change by 10%.
# (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
# xlarge=1300) Use static concept.

class Shirt:

    # Static variable
    size_increment = 10

    # Constructor - parameterized and parameterless
    def __init__(self, sid=0, sname="", type="formal", price=0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    # Getter and Setter for sid
    def getsid(self):
        return self.sid

    def setsid(self, new_sid):
        self.sid = new_sid

    # Getter and Setter for sname
    def getsname(self):
        return self.sname

    def setsname(self, new_sname):
        self.sname = new_sname

    # Getter and Setter for type
    def gettype(self):
        return self.type

    def settype(self, new_type):
        self.type = new_type

    # Getter and Setter for price
    def getprice(self):
        return self.price

    def setprice(self, new_price):
        self.price = new_price

    # Getter and Setter for size
    def getsize(self):
        return self.size

    def setsize(self, new_size):
        self.size = new_size

    # Apply size-wise price
    def apply_size_price(self):

        if self.size == "small":
            self.price = self.price

        elif self.size == "medium":
            self.price = self.price + (self.price * Shirt.size_increment / 100)

        elif self.size == "large":
            self.price = self.price + (self.price * 2 * Shirt.size_increment / 100)

        elif self.size == "xlarge":
            self.price = self.price + (self.price * 3 * Shirt.size_increment / 100)

    # Destructor
    def __del__(self):
        print("Shirt is destroyed")

    # ShowBook
    def ShowBook(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Shirt Type:", self.type)
        print("Shirt Price:", self.price)
        print("Shirt Size:", self.size)


# Create object
a1 = Shirt(1, "Cotton Shirt", "T-Shirt", 1000, "large")

# Apply size price
a1.apply_size_price()

# Display
a1.ShowBook()


def sizeprice(self):
    if size="small"
        self.price=self.price
