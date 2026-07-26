# Q9)Input 5 subject marks from user and display grade(eg.First class,Second class ..)
s1=int(input("enter the marks of subject :"))
s2=int(input("enter the marks of subject :"))
s3=int(input("enter the marks of subject :"))
s4=int(input("enter the marks of subject :"))
s5=int(input("enter the marks of subject :"))
total_marks=500
obtained_marks=s1+s2+s3+s4+s5
print(obtained_marks)
percentage=(obtained_marks/total_marks)*100
print("percentage is ",percentage)
if(percentage>=90):
    print("Grade is O")
elif(percentage>=80):
    print("Grade is A")
elif(percentage>=70):
    print("Grade is B")
elif(percentage>=60):
    print("Grade is c ")
elif(percentage>=50):
    print("Grade is c")
elif(percentage <50):
    print("do study properly")