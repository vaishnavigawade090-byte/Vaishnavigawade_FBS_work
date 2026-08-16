# Q7). Write a program to create a new list from existing list which contains cube of each number of list.
li=[1,2,3,4,5,6,7,8,9,10]
cube_li=[]
for i in range(0,len(li)-1):
    cube= li[i]**3
    cube_li.append(cube) 
print("original list",li)
print("cube list",cube_li)
