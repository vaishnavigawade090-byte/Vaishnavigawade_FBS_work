# 4. Write a program to find sum of n numbers using recursion.
def sos(n):
    if(n>0):
        return n+ sos(n-1)
    else:
        return 0
n=int(input("enter the number :"))
res=sos(n)
print(res)