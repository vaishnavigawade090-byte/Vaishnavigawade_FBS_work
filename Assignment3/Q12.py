# 12. Write a program to check if given 3 digit number is a palindrome or not.
num =int(input("enter the 3 digit number :"))
temp=num
d1 =num%10
num =num//10
d2= num%10
num= num//10
d3= num%10
num =num//10
print(num)
if d1 == d3:
    print(temp, "is a palindrome number.")
else:
    print(temp, "is not a palindrome number.")

