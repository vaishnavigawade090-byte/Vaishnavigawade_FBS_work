# Python Assignment – (Operator Overloading)

# 1. Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator


#constructor
class Complexnumber:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

#Destructor
    def __del__(self):
        print("object is going to out of scope")


#c.
#  Overload + operator
    def __add__(self,other):
        return Complexnumber(self.real+ other.real,
                             self.imag+ other.imag)

##overload _operator
    def __sub__(self,other):
        return Complexnumber(self.real- other.real,
                             self.imag- other.imag)
    
#display
    def __str__(self):
        return f"{self.real}+{self.imag}i"   ##str used for readeable format

#objects
o1=Complexnumber(5,3)
o2=Complexnumber(3,6)
o3= o1+o2
o4=o1- o2
print(o1)
print(o1)
print("Addition:", o3)
print("Subtraction:", o4)
