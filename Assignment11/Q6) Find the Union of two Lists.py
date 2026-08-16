# Q6). Python Program to Find the Union of two Lists

l1 = [1, 2, 3, 4]
l2 = [2, 4, 5, 6]

union = []

for i in l1:
    if i not in union:
        union.append(i)

for i in l2:
    if i not in union:
        union.append(i)

print(union)