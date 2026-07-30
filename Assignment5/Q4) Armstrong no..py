#Q4). WAP to print Armstrong number within a given range

# start=int(input("enter the starting range: "))
# end=int(input("enter the ending range :"))
# for num in range(start,end+1):
#     original=num
#     power=len(str(num))
#     sum=0
#     while(num >0):
#         d=num%10
#         sum= sum+d**power
#         num= num//10
    
#         if(sum==original):
#             print(f'{num} is a armstrong number')
        


start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))


for num in range(start, end+1):
    original = num
    power = len(str(num))
    sum = 0

    while(num > 0):
        d = num % 10
        sum = sum + d ** power
        num = num // 10

    if(sum == original):
        print(original, "is an Armstrong number")



    

