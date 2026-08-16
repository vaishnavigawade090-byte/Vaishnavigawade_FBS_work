#Q7) Count frequency of each word in a string

str1 = "hello world hello python world hello"

words = str1.split()
dict1 = {}

for i in words:
    if i in dict1:
        dict1[i] = dict1[i] + 1
    else:
        dict1[i] = 1

print(dict1)