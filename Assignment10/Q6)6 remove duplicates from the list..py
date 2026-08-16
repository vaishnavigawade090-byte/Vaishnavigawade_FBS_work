# Q6). Write a program to remove duplicates from the list.
li=[10,40,40,34,56,56,78]
new_li = []

for i in li:
    flag = 0
    for j in new_li:
        if i == j:
            flag = 1
            break
    
    if flag == 0:
        new_li.append(i)

print("Original list:", li)
print("List after removing duplicates:", new_li)
