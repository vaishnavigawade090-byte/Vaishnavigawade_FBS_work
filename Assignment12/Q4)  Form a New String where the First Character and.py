# Q4). Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged
str="abhirani"
new_str=" "
size=len(str)
print(size)
for i in range(size):
    if i==0:
        new_str= new_str + str[size-1]
    elif i==size-1:
        new_str=new_str+str[0]
    else:
        new_str=new_str+str[i]
print(new_str)