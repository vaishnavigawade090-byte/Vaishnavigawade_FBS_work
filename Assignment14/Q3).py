# Q3) Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set
# data type.

words = ["apple", "banana", "apple", "orange", "banana", "apple"]

unique_words = set(words)

for word in unique_words:
    count = 0

    for i in words:
        if word == i:
            count += 1

    print(word, "=", count)