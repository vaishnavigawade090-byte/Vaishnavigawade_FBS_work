# 11. WAP to check if a given number is Armstrong number or not.

def armstrong():
    num = int(input("Enter the number: "))
    temp = num
    sum = 0
    count = 0
    
    # Count number of digits
    while(temp > 0):
        count = count + 1
        temp = temp // 10
        
    temp = num
    
    # Calculate Armstrong value
    while(temp > 0):
        d = temp % 10
        sum = sum + (d ** count)
        temp = temp // 10
        
    return num == sum

res = armstrong()
print(res)