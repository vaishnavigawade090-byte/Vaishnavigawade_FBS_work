# Q14) Python Program to Count the Occurrences of Each Word in a String

str = "hello world hello python world hello"

words = str.split()

for i in range(len(words)):
    count = 0

    for j in range(len(words)):
        if words[i] == words[j]:
            count += 1

    already = False

    for k in range(i):
        if words[i] == words[k]:
            already = True

    if already == False:
        print(words[i], "=", count)