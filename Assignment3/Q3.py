# Q3)Write a program to input angles of a triangle and check whether triangle is valid or not.
a1=int(input("enter angle 1 :"))
a2=int(input("enter angle 2 :"))
a3=int(input("enter angle 3 :"))
sum=a1+a2+a3
if(sum==180):
    print('triangle is valid')
else:
    print('triangle is not valid')