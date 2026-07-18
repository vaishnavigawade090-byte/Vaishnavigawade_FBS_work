#Q6) Write a Program to input two angles from user and find third angle of the triangle.
angle1=int(input("enter a 1st angle : "))
angle2=int(input("enter a 2nd trianglev: "))
#we know the sum of triangle is 180
angle3=180-(angle1+angle2)
print(f"third angle of the triangle is {angle3}")
