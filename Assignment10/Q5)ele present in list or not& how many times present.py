#Q5) 5. Accept a number from user and check if this element is present in the list or 
# not. Also tell how many times it is present in the list.
li = [45, 76, 54, 87, 66, 46]
n = int(input("Enter the number: "))
count = 0

for i in range(len(li)):
    if li[i] == n:
        count = count + 1

if count > 0:
    print("Number is present in the list")
    print("It is present", count, "times")
else:
    print("Number is not present in the list")