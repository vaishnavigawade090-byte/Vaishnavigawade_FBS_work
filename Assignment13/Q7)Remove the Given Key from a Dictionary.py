#Q6) Remove a given key from a dictionary

dict1 = {"name": "Vaishnavi", "age": 22, "city": "Pune"}

key = input("Enter key to remove: ")

if key in dict1:
    del dict1[key]
    print("Dictionary after removing key =", dict1)
else:
    print("Key does not exist")