#10). WAP to check if given number is Perfect Number.
# A Perfect Number is a positive integer that is equal to the sum of its proper divisors
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum += i

if sum == n:
    print("Perfect number")
else:
    print("Not a perfect number")