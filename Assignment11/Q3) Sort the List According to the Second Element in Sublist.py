# Q3)WAP to Sort the List According to the Second Element in Sublist
li = [[1, 50], [2, 20], [3, 40], [4, 10]]

li.sort(key=lambda x: x[1])

print(li)