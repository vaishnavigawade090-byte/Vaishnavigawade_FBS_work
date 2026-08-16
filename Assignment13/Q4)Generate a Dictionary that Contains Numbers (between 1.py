#Q4) Generate dictionary in the form (x, x²)

n = int(input("Enter n: "))

dict1 = {}

for x in range(1, n + 1):
    dict1[x] = x * x

print(dict1)