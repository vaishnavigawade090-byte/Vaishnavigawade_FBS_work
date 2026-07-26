# Q9) WAP to print all numbers in a range divisible by a given number.
n=int(input("enter the number : "))
num=int(input("enter the divisor number "))
for i in range(1,n+1):
    if(i%num==0):
        print(i,end=' ')
print()