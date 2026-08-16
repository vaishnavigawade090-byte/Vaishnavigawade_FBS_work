# Q5)Python Program to Count the Number of Vowels in a String
str="anvi"
size=len(str)
count=0
for ch in str :
    if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
        count+=1
print(count)