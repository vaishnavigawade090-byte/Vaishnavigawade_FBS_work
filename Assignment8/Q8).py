# 8. Write a program find reverse of a number
def reverse_num():
    num = int(input("Enter the number: "))
    rev = 0
    
    while(num > 0):
        d = num % 10
        rev = rev * 10 + d
        num = num // 10
        
    return rev

res = reverse_num()
print(res)