# Q8) Check whether a number is prime using recursion

num = int(input("Enter a number: "))

def prime(n, i):
    if n <= 1:
        return False
    if i == n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)

if prime(num, 2):
    print("Prime number")
else:
    print("Not a prime number")