# Q2)Python Program to Remove the nth Index Character from a Non-Empty String.
str="Life is very beautiful"
n=int(input("enter the number: "))
new_str=" "
size=len(str)
for i in range(0,size):
    if i!=n:
        new_str=new_str+str[i] 
print(new_str)
