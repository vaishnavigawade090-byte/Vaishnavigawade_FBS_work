# Q10) Remove all occurrences of a given element from the list

li = [10, 20, 30, 20, 40, 20, 50]

n = int(input("Enter element to remove: "))

new_li = []

for i in li:
    if i != n:
        new_li.append(i)

print("Original list:", li)
print("List after removing:", new_li)