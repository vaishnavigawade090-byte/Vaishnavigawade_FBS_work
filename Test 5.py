# #Q1)1. A list contains the denominations as follows :
# D = [2000, 500, 200, 100 , 50, 20, 10, 5]
# Accept an amount from user and calculate how many
# minimum number of notes will be needed for that
# amount.

# D=[2000,500,200,100,50,20,10,5]
# amount=int(input("enter the ammount :"))
# count=0
# for note in D:
#     count=count+amount//note
#     amount=amount % note
# print(f"minimum number of notes is {count}")


# Q5)Python Program to Find the Union of two Lists without
# using set concept.
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# l=l1+l2
# print(l)

# Q2)
# n = int(input("Enter number of coins: "))
# coins = list(map(int, input().split()))

# missing = 0

# for coin in coins:
#     missing = missing ^ coin

# print("Missing coin =", missing)


# Q3) A list contains sublist with Emp information as follows :
# Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
# [210,”Tannu”,14000],[320,”Suresh”,35000]]
# Write a program to sort the list based on salary
# Data = [[101, "Seema", 45000],
#         [340, "Rajani", 13000],
#         [210, "Tannu", 14000],
#         [320, "Suresh", 35000]]

# Data.sort(key=lambda x: x[2])

# print(f"sorted salary is {Data}")

#Q4)There is a list with some numbers. Create a new
# dictionary using this list in such a way that key is
# number and value is frequency of occurrence of that
# number in list.
# [1,3,4,1,2,3,6,7,1,2,4]
# {1:3,3:2,2:2,

li = [1,3,4,1,2,3,6,7,1,2,4]

D = {}

for x in li:
    D[x] = li.count(x)

print(D)

