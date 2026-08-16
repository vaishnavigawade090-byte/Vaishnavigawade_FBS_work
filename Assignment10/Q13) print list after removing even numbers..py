# Q13) Write a program to print list after removing even numbers.
li = [12, 23, 56, 41, 89, 14, 25]

new_li = []

for i in li:
    if i % 2 != 0:
        new_li.append(i)

print("List after removing even numbers:", new_li)