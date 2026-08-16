# Q7) Find sum of digits using recursion

num = int(input("Enter a number: "))

def sum_digits(n):
    if n == 0:
        return 0

    digit = n % 10
    return digit + sum_digits(n // 10)

result = sum_digits(num)

print("Sum of digits =", result)