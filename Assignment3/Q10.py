# 10. Write a program to check if person is eligible to marry or not (male age >=21 and female age>=18)
gender=input("enter the gender of the person:")
age= int(input("enter the age of the person :"))
if(gender=="f"):
    if(age>=18):
        print("eligible to marriage ")
    else:
        print("first complete your education")
elif gender=='m':
    if(age>21):
        print("eligible to marriage ")
    else:
        print("complete your education and make your carrier")
