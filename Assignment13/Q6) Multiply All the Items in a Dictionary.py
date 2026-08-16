# Q6)Multiply all values in a dictionary

dict1 = {"a": 2, "b": 3, "c": 4, "d": 5}

multiply = 1

for i in dict1:
    multiply = multiply * dict1[i]

print("Multiplication of all items =", multiply)