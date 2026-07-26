# Q6)WAP to check if a given number is prime number or not.
# to check given number is prime or not
#the no. is divisible by 1 and itself
num=int(input("enter the number :"))
if(num>1):
    for i in range(2,num//2+1):     ## num//2+1 is wrriten due to reduce execution. no need to be execute unwanted iteration
        print(i)
        if(num %i==0):
            print(f'{num} is not a prime number')
            break
    else:
        print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')