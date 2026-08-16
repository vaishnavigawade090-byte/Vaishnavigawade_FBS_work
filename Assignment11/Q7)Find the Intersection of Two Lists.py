# Q7) Python Program to Find the Intersection of Two Lists
l1 = [1, 2, 3, 4]
l2 = [2, 4, 5, 6]

intersection = []

for i in l1:
    if i in l2:
        intersection.append(i)
        
print(intersection)