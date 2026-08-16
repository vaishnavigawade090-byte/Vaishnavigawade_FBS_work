# Q12) Create three lists of numbers, their squares and cubes

li = [1, 2, 3, 4, 5]

square = []
cube = []

for i in li:
    square.append(i ** 2)
    cube.append(i ** 3)

print("Numbers :", li)
print("Squares :", square)
print("Cubes   :", cube)