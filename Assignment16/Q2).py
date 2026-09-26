# Q2) Create a class Product with members as pid,pname,price and quantity .Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static member discount.
# f. Provide methods for applying discount on price of product.

class Product:

    # Static member
    discount = 10

    # Constructor
    # Supports parameterized and parameterless
    def __init__(self, pid=0, pname="", price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    # Destructor
    def __del__(self):
        print("Product object destroyed")

    # ShowProduct method
    def ShowProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # Method for applying discount
    def apply_discount(self):
        self.price = self.price - (self.price * Product.discount / 100)


# Parameterized object
p1 = Product(101, "Laptop", 50000, 2)

print("Before Discount:")
p1.ShowProduct()

# Apply discount
p1.apply_discount()

print("\nAfter Discount:")
p1.ShowProduct()

print("\nDiscount:", Product.discount, "%")
    