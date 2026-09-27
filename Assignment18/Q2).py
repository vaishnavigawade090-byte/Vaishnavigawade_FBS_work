# Q2). Create a class Distance with data members as km, m and cm
# a. Constructor
# b. Destructor
# c. Overload +, - operator


# Constructor
class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    # Destructor
    def __del__(self):
        print("Object is going to out of scope")

    # Overloading + operator
    def __add__(self, other):
        return Distance(self.km + other.km,
                        self.m + other.m,
                        self.cm + other.cm)

    # Overloading - operator
    def __sub__(self, other):
        return Distance(self.km - other.km,
                        self.m - other.m,
                        self.cm - other.cm)

    # Display
    def __str__(self):
        return f"{self.km} km + {self.m} m + {self.cm} cm"


# Objects
o1 = Distance(100, 10, 5)
o2 = Distance(200, 100, 50)

print(o1)
print(o2)

o3 = o1 + o2
o4 = o1 - o2

print("Addition is:", o3)
print("Subtraction is:", o4)