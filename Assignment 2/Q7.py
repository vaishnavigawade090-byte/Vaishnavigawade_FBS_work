# Q7) WAP sum of three digit number
num=int(input("Enter the three digit number :"))
d1=num%10
print(d1)
num=num//10
print(num)
d2=num%10
print(d2)
num=num//10
print(num)
d3=num%10
print(d3)
num=num//10
print(num)
sum=d1+d2+d3
print(sum)
