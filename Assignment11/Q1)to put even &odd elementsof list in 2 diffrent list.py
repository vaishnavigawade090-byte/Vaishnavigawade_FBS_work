# Q1). Python Program to Put Even and Odd elements of a List into two Different Lists

li=[10,20,30,40,50,60,70,80,42,45]

li_even = []
li_odd = []
for i in li:
    if i % 2 == 0:
        li_even.append(i)
    else:
        li_odd.append(i)

print(li_even)
print(li_odd)
