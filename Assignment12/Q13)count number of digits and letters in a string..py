# Q13). Python Program to count number of digits and letters in a string.

str = "Hello123World"

digit = 0
letter = 0

for i in str:
    if i >= '0' and i <= '9':
        digit += 1
    elif (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        letter += 1

print("Number of digits =", digit)
print("Number of letters =", letter)