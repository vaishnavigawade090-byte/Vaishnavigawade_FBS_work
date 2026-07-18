# Q9). Write a program to swap two numbers without using third variable.
# x=int(input("enter a number :"))
# y=int(input("enter a number :"))
# x,y=y,x
# print(x)
# print(y)

#another way    
x=int(input("enter a number :"))
y=int(input("enter a number :"))
x=x+y
y=x-y
x=x-y
print(x)
print(y)

