#Q3) Write a program to find sum of following series using functions :
# a). 1+ 2 + 3 + 4+..... + n
n=int(input("enter the number :"))
def sum(n):
    if n>0:
        return n+ sum(n-1)
    else:
        return 0
res=sum(n)
print(res)

