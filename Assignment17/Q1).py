# Python Inheritance Assignment

# Q1).Create a class Student with following
# a. data members :
# i. StudentId
# ii. Name
# iii. Age
# iv. Percentage

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. Method CalculateRank
# v. Override __str__ Method


class Student:

    # i. Parameterized Constructor
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    # ii. Display
    def Display(self):
        print("Student ID :", self.StudentId)
        print("Name       :", self.Name)
        print("Age        :", self.Age)
        print("Percentage :", self.Percentage)

    # iii. Accept
    def Accept(self):
        self.StudentId = int(input("Enter Student ID : "))
        self.Name = input("Enter Name : ")
        self.Age = int(input("Enter Age : "))
        self.Percentage = float(input("Enter Percentage : "))

    # iv. CalculateRank
    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    # v. Override __str__ method
    def __str__(self):
        return f"Student ID: {self.StudentId}, Name: {self.Name}, Age: {self.Age}, Percentage: {self.Percentage}"


# Object creation
o1 = Student(101, "Vaishnavi", 22, 91.8)

# Display
o1.Display()

# Calculate Rank
print("Rank :", o1.CalculateRank())

# __str__
print(o1)
            


