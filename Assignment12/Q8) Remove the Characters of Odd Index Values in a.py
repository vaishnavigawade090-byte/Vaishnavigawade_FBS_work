# Q8)Python Program to Remove the Characters of Odd Index Values i
# n a String
str = "Everything is my mom and dad "
new_str = ""

for i in range(0, len(str), 2):
    new_str = new_str + str[i]

print(new_str)