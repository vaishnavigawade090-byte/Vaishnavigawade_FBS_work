# Write a program which calculates toll calculation on some location following is data provided:
# Many vehicles goes through the toll every vehicle has to pay the basic  toll + extra charges if any.
# two wheelers have to pay basic toll Rs 20 three wheelers have to pay
# 30 and four wheelers have to pay 40 heavy veheicles i.e. Vehicles having wheels more than four, have to
# pay 60 Rs as basic toll extra charges :
# for two wheelers if no. of persons are more than two extra charge
# =10/person
# for three wheelers if no. of persons are more than 3 extra charge
# =20/person
# for four wheelers if no. of persons are more than 4 extra charge
# =40/person
# for heavy vehicle if no. of person are more than 6 extra charges
# =100/person.
# Show polymorphic behaviour in main. Main module should be
# designed in such way that toll should easily operate it through
# interactive menu driven program .
# Object of vehicle class should not be possible.



from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self, persons):
        pass


# Two Wheeler
class TwoWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 20

        if persons > 2:
            toll = toll + (persons - 2) * 10

        return toll


# Three Wheeler
class ThreeWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 30

        if persons > 3:
            toll = toll + (persons - 3) * 20

        return toll


# Four Wheeler
class FourWheeler(Vehicle):

    def calculate_toll(self, persons):
        toll = 40

        if persons > 4:
            toll = toll + (persons - 4) * 40

        return toll


# Heavy Vehicle
class HeavyVehicle(Vehicle):

    def calculate_toll(self, persons):
        toll = 60

        if persons > 6:
            toll = toll + (persons - 6) * 100

        return toll


# Main program
while True:

    print("\n----- TOLL MENU -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        v = TwoWheeler()

    elif choice == 2:
        v = ThreeWheeler()

    elif choice == 3:
        v = FourWheeler()

    elif choice == 4:
        v = HeavyVehicle()

    else:
        print("Invalid choice")
        continue

    print("Total Toll = Rs.", v.calculate_toll(persons))