# Q5). Python Program to Sum All the Items in a Dictionary
# Sum all values in a dictionary

dict1 = {"a": 10, "b": 20, "c": 30, "d": 40}

sum = 0

for i in dict1:
    sum = sum + dict1[i]

print("Sum of all items =", sum)