#  Q9)Write a program to check if entered number is a palindrome or not.

def chkpalindrome(num):
    temp = num
    rev = 0
    
    while temp > 0:
        d = temp % 10
        rev = rev * 10 + d
        temp = temp // 10
        
    if num == rev:
        return True
    else:
        return False


num = int(input("Enter the number: "))

print(chkpalindrome(num))



