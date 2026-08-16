# Q1). Write a program to find sum of following series using recursive 
# functions:

# i) 1! + 2! + 3! + 4! +..... + n!

n = int(input("Enter n: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def series_sum(n):
    if n == 0:
        return 0
    return factorial(n) + series_sum(n - 1)

result = series_sum(n)

print("Sum of series =", result)