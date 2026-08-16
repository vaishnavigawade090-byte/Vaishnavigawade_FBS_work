# Q4) Find all pairs of elements whose sum is equal to a given value

li = [2, 4, 3, 5, 7, 8, 1]
num = int(input("Enter the sum value: "))

for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == num:
            print(li[i], li[j])