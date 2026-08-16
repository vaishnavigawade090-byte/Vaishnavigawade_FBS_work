# 5. Write a program to find factorial using recursion.

def sof(n):
    if(n>0):
        return n* sof(n-1)
    else:
        return 1
n=int(input("enter the number :"))
res=sof(n)
print(res)