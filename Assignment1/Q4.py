#Q4)Write a program to enter P,T,R and calculate the simple interest
P=int(input("enter Principal_val :"))
T=int(input("enter  Time in years :"))
R=int(input("enter Rate of interest :"))
#perform operation
simple_interest = (P*R*T)/100
print("simple interest is",simple_interest)