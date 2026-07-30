# Q3)Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.


passengers = int(input("Enter number of passengers: "))
ticket_cost = int(input("Enter per ticket cost: "))

total_amount = 0

for i in range(1, passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))

    if age < 12:
        cost = ticket_cost - (ticket_cost * 30 / 100)
        print("Child ticket cost:", cost)

    elif age > 59:
        cost = ticket_cost - (ticket_cost * 50 / 100)
        print("Senior citizen ticket cost:", cost)

    else:
        cost = ticket_cost
        print("Normal ticket cost:", cost)

    total_amount = total_amount + cost

print("Total amount to travel =", total_amount)