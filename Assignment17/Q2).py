# Q2). Create a derived class from Student as EnggStudent with :
# a. Data members as :
# i. Branch
# ii. InternalMarks

# b. Add the following methods :
# i. Parameterized constructor
# ii. Display
# iii. Accept
# iv. override Method CalculateRank
# v. Override __str__ Method

class Student:

    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

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


class EnggStudent(Student):

    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)

        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Display(self):
        print("StudentId :", self.StudentId)
        print("Name :", self.Name)
        print("Age :", self.Age)
        print("Percentage :", self.Percentage)
        print("Branch :", self.Branch)
        print("Internal Marks :", self.InternalMarks)

    def Accept(self):
        self.StudentId = int(input("Enter Student ID : "))
        self.Name = input("Enter Name : ")
        self.Age = int(input("Enter Age : "))
        self.Percentage = float(input("Enter Percentage : "))
        self.Branch = input("Enter Branch : ")
        self.InternalMarks = float(input("Enter Internal Marks : "))

    def CalculateRank(self):
        if self.Percentage >= 75 and self.InternalMarks >= 40:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return (f"StudentId: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}, "
                f"Branch: {self.Branch}, "
                f"Internal Marks: {self.InternalMarks}")


# Object creation
e1 = EnggStudent(101, "Vaishnavi", 22, 91.8, "Computer", 45)

e1.Display()

print("Rank :", e1.CalculateRank())

print(e1)