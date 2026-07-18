#Q4)Write a program toenter P,T,R and calculate the compound interest
Principal_val=int(input("enter the principal  value :"))
Time=int(input("enter the time :"))
Rate=int(input("enter the rate of interest :"))
#compound interest=A-P
# Amount= A =P*(1+R/100)^T
Amount=(Principal_val*((1+Rate/100)**Time))
print(Amount)
compound_interest=Amount-Principal_val
print("compound_interest is ",compound_interest)

