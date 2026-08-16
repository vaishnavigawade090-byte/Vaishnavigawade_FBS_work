# Q15) Python Program to Find Larger String
# Without Using Built-in Functions

str1 = "Hello"
str2 = "Everything"

count1 = 0
count2 = 0

for i in str1:
    count1 += 1

for i in str2:
    count2 += 1

if count1 > count2:
    print("Larger string =", str1)
elif count2 > count1:
    print("Larger string =", str2)
else:
    print("Both strings are equal")