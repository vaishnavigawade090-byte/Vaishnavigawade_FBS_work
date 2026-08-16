# Q4) Sum of all odd numbers between 1 to n

n = int(input("Enter the number: "))

def odd_sum(n):
    sum = 0
    
    for i in range(1, n+1):
        if i % 2 != 0:
            sum = sum + i
            
    return sum

res = odd_sum(n)

print("Sum of odd numbers:", res)