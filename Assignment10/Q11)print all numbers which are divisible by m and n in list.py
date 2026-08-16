# Q11) Write a program to print all numbers which are divisible by m and n in the list.

li = [12, 23, 56, 41, 89, 12, 14]

m = int(input("Enter m: "))
n = int(input("Enter n: "))

for i in li:
    if i % m == 0 and i % n == 0:
        print(i)