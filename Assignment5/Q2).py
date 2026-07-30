#Q2) Enter number of students from user. For those many students accept marks of 5
n = int(input("Enter number of students: "))

for i in range(1, n+1):
    print("Enter marks for Student", i)

    total = 0

    for j in range(1, 6):
        marks = int(input(f"Enter marks of subject {j}: "))
        total = total + marks

    print("Total marks of Student", i, "=", total)
    print("---------------------")