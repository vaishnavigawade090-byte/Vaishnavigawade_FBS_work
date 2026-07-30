# 1). Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.
userid = "admin"
password = "12345"

count = 1

while count <= 3:
    user_id = input("Enter User ID: ")
    user_pass = input("Enter Password: ")

    if user_id == userid and user_pass == password:
        print("Login successful")
        break
    else:
        print("Incorrect User ID or Password")
        print("Attempts left:", 3 - count)

    count += 1

if count > 3:
    print("Account blocked. Try after some time.")