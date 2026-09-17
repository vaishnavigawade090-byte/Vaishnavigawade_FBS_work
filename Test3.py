#Q1) Write a program to print first n prime numbers
n=int(input("enter the number "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1

if count == 2:
    print("n is prime")
else:
    print("n is not prime")


#Q2)Write a program to calculate the sum of following series  where n is input by user.
#  1/1! + 2/2! + 3/3! + 4/4! + ... N/N!
n = int(input("Enter the number: "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (i / fact)

print("Sum =", sum)

# Q3)Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

n = int(input("Enter the no of employee: "))

da = 0.10
ta = 0.12
hra = 0.15

total_all = 0

for i in range(1, n + 1):

    b_sal = int(input("Enter the basic salary of the employee: "))

    if b_sal < 20000:

        total_sal = b_sal + (b_sal * da) + (b_sal * ta) + (b_sal * hra)

        print("Total salary =", total_sal)

    else:

        total_sal = b_sal + (b_sal * 0.15) + (b_sal * 0.18) + (b_sal * 0.20)

        print("Total salary =", total_sal)

    total_all = total_all + total_sal

print("Total salary of all employees =", total_all)


# 4. Write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101
 
n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i+j) % 2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()

