#Q8) Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
userid=input("enter user id : ")
password=input("enter the password :")
if userid =="admin" and password== "virat@123":
    captch=random.randint(1000,9999)
    print(f"your captcha ={captch}")
    chuser=int(input("enter the captcha=>"))
    if chuser==captch:
        print("user login sucessfully ")
    else:
        print("invalid captcha ")
else:
    print("user is invalid ")


