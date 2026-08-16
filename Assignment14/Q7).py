# Q7) Find missing numbers in the second set as compared to the first and vice versa

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

missing_in_set2 = set1 - set2
missing_in_set1 = set2 - set1

print("Numbers missing in set2 =", missing_in_set2)
print("Numbers missing in set1 =", missing_in_set1)