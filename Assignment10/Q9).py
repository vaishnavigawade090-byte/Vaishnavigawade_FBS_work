# Q9). Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.
li=[11,12,13,14,15,16,17,18]
even_li=[]
odd_li=[]
for i in li:
    if i%2==0:
        even_li=even_li+[i]
    else:
        odd_li=odd_li+[i]
print(f"even number is {even_li}")
print(f"odd number is {odd_li}")
