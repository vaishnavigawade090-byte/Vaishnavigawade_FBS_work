# Q9) Write a program to create three lists of numbers,
#  their squares and cubes
li1=[1,2,3,4,5,6]
li2=[]
li3=[]
print(li1)
for i in li1:
    sq=i**2
    cu=i**3
    li2.append(sq)
    li3.append(cu)
print("square is",li2)
print("cube is ",li3)
    

