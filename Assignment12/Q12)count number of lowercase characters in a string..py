# Q12) Python Program to Count Number of Lowercase Characters in a String

str = "Hello Everyone"

count = 0

for i in str:
    if i >= 'a' and i <= 'z':
        count += 1

print("Number of lowercase characters =", count)