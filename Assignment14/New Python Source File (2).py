# Q9) Find unique combinations of 3 numbers
# whose sum is equal to a target number

li = [1, 2, 3, 4, 5, 6]
target = int(input("Enter target number: "))

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        for k in range(j + 1, len(li)):
            if li[i] + li[j] + li[k] == target:
                print(li[i], li[j], li[k])