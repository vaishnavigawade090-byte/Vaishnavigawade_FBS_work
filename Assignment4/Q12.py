# Q12)Write a program to check if given number is Armstrong number or not.
num = int(input("Enter the number: "))
temp = num
count = 0

# Count the number of digits
while(temp > 0):
    count = count + 1
    temp = temp // 10

temp = num
sum = 0

# Find the sum of digits raised to the power 'count'
while(temp > 0):
    digit = temp % 10
    sum = sum + (digit ** count)
    temp = temp // 10

if(sum == num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
