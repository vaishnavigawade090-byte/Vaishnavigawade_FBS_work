# Q11) Python Program to Replace Every Blank Space with Hyphen in a String

str = "hello everyone how are you"
new_str = ""

for i in str:
    if i == " ":
        new_str = new_str + "-"
    else:
        new_str = new_str + i

print(new_str)