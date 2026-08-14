# #Q1)
n = int(input("Enter n: "))

count = 0
num = 2

while count < n:
    count1 = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count1 = count1 + 1

    if count1 == 2:
        print(num, end=" ")
        count = count + 1

    num = num + 1

# # Q2)

# n = int(input("Enter n: "))

# sum = 0
# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + (i / fact)

# print("Sum of series =", sum)



# # Q3)

# n = int(input("Enter number of employees: "))

# total = 0

# for i in range(n):
#     basic = float(input("Enter basic salary: "))

#     if basic < 20000:
#         da = basic * 10 / 100
#         ta = basic * 12 / 100
#         hra = basic * 15 / 100
#     else:
#         da = basic * 15 / 100
#         ta = basic * 18 / 100
#         hra = basic * 20 / 100

#     salary = basic + da + ta + hra

#     print("Total salary =", salary)

#     total = total + salary

# print("Total salary of all employees =", total)


# # Q4)

# # for i in range(1,6):
# #     for j in range(1,6):
# #         if(i+j)%2==0:
# #             print(1,end=" ")
# #         else:
# #             print(0,end=" ")
# #     print()



