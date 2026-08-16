#Q8). Write a program to create a duplicate of an existing list. It should not point to same list

li = [10, 20, 30, 40, 50]
dup = []

for i in li:
    dup.append(i)

print("Original list:", li)
print("Duplicate list:", dup)

# checking different memory location
print(li is dup)