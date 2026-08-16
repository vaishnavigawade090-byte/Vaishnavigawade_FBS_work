# Q4)Write a program to reverse the list.
li=[10,20,30,40,50]
size=len(li)

for i in range(size // 2):
    temp = li[i]
    li[i] = li[size - 1 - i]
    li[size - 1 - i] = temp

print(li)