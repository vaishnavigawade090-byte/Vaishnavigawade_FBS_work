# Q3)Python Program to Check if a Given Key Exists in a Dictionary or Not

dict1 = {"name": "Vaishnavi", "age": 22, "city": "Pune"}

key = input("Enter key to search: ")

if key in dict1:
    print("Key exists in dictionary")
else:
    print("Key does not exist in dictionary")