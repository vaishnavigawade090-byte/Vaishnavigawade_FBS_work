# Q2)WAP to print all odd numbers until n.
n=int(input(" Enter the number :"))
i=1
while(i<=n):
    if(i%2!=0):
        print("odd number is ",i)
    i+=1