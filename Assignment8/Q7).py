# 7. Write a program to find sum of digits of a number.
def sum():
    num=int(input("enter the number :"))
    temp=num
    sum=0
    while(temp>0):
        d=temp % 10
        sum=sum+d
        temp=temp//10            #change value
    return sum
res=sum()
print(res)