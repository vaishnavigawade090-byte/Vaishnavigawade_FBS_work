# Q3)WAP to find second largest element in list
li=[45,67,34,89,46,35,78]
largest = li[0]
second = li[0]

for i in range(1, len(li)):
    if li[i] > largest:
        second = largest
        largest = li[i]
    elif li[i] > second and li[i] != largest:
        second = li[i]

print("Second largest element is:", second)