# Write a program to calculate profit or loss.
cost_price =int(input("enter price of product :"))
selling_price =int(input("enter selling price :"))
cost= selling_price-cost_price
if cost>0:
    print("profit")
else:
    print("loss")