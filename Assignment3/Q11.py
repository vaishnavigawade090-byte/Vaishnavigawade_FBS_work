# 11. Accept age of five people and also per person ticket amount and then calculate total
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
ag1=int(input("enter the age of first person:"))
tkprice1=float(input("enter the ticket price of first person :"))
totalprice=0
if ag1<12:
    totalprice=totalprice+(tkprice1*0.30)
elif ag1>59:
    totalprice=totalprice+(tkprice1*0.50)
else:
    totalprice=totalprice+tkprice1
#first person share ends here...
ag2=int(input("enter the age of second  person:"))
tkprice2=float(input("enter the ticket price of second person :"))
totalprice=0
if ag2<12:
    totalprice=totalprice+(tkprice2*0.30)
elif ag2>59:
    totalprice=totalprice+(tkprice2*0.50)
else:
    totalprice=totalprice+tkprice2


