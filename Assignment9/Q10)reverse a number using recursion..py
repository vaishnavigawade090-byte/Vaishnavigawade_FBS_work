# Q10) Reverse a number using recursion

num = int(input("Enter a number: "))

def reverse(n, rev):
    if n == 0:
        return rev

    digit = n % 10
    rev = rev * 10 + digit

    return reverse(n // 10, rev)

result = reverse(num, 0)

print("Reverse number =", result)