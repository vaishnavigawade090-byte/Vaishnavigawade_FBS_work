# Q6) Print Fibonacci series using recursion

n = int(input("Enter number of terms: "))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(n):
    print(fibonacci(i), end=" ")