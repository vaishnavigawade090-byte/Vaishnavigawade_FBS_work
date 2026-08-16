# 6. Write a program to find print the following Fibonacci series using
# functions:
# 1 1 2 3 5 8 n terms
n = int(input("Enter number of terms: "))

def fibonacci(n):
    a = 1
    b = 1
    
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

fibonacci(n)