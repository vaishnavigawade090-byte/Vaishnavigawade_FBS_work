# Q8)8. Write a Python program to find all the anagrams and group them
# together from a given list of strings.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for word in words:
    key = ""

    # Sort characters manually
    for ch in word:
        key = key + ch

    chars = list(key)

    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            if chars[i] > chars[j]:
                temp = chars[i]
                chars[i] = chars[j]
                chars[j] = temp

    key = ""
    for ch in chars:
        key = key + ch

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

for key in groups:
    print(groups[key])