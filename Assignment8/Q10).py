# 10. Write a program to check if entered year is a leap year or not.

def leap_year():
    year = int(input("Enter the year: "))
    
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

res = leap_year()
print(res)