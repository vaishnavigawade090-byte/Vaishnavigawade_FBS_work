li=[30,45,23,76,35]
max=li[0]
for ind in range(1,len(li)):
    if (li[ind]> max):
        max=li[ind]
print(f" maximum number is{max}")

min=li[0]
for ind in range(1,len(li)):
    if (li[ind]< min):
        min=li[ind]
print(f" Minimum number is {min}")

