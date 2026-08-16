# Q9)Python Program to Calculate the Number of Words and
# the Number of Characters Present in a String

str = "Everything is my mom and dad"

words = 0
characters = 0

for i in str:
    characters += 1

for i in str.split():
    words += 1

print("Number of words =", words)
print("Number of characters =", characters)