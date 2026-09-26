# Q3). Create a class MedicalStudent inherited from Student with following
# :

# i. Data members :Specialization
# ii. MarksOfInternship
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


# Q3: MedicalStudent inherited from Student
class MedicalStudent(Student):

    # i. Parameterized Constructor
    def __init__(self, StudentId, Name, Age, Percentage,
                 Specialization, MarksOfInternship):

        super().__init__(StudentId, Name, Age, Percentage)

        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    # ii. Display
    def Display(self):
        print("StudentId :", self.StudentId)
        print("Name :", self.Name)
        print("Age :", self.Age)
        print("Percentage :", self.Percentage)
        print("Specialization :", self.Specialization)
        print("Marks Of Internship :", self.MarksOfInternship)

    # iii. Accept
    def Accept(self):
        self.StudentId = int(input("Enter Student ID : "))
        self.Name = input("Enter Name : ")
        self.Age = int(input("Enter Age : "))
        self.Percentage = float(input("Enter Percentage : "))
        self.Specialization = input("Enter Specialization : ")
        self.MarksOfInternship = float(
            input("Enter Marks Of Internship : ")
        )

    # iv. Override CalculateRank
    def CalculateRank(self):
        if self.Percentage >= 75 and self.MarksOfInternship >= 40:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    # v. Override __str__
    def __str__(self):
        return (f"StudentId: {self.StudentId}, "
                f"Name: {self.Name}, "
                f"Age: {self.Age}, "
                f"Percentage: {self.Percentage}, "
                f"Specialization: {self.Specialization}, "
                f"Marks Of Internship: {self.MarksOfInternship}")


# Object creation
m1 = MedicalStudent(
    102,
    "Vaishnavi",
    22,
    91.8,
    "Cardiology",
    45
)

m1.Display()

print("Rank :", m1.CalculateRank())

print(m1)