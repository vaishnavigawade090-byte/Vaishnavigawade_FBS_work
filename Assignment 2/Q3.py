# Q3)Convert distantance  given in feet and inches into meter and centimeter.
feet=int(input("enter distancr in feet: "))
inch=int(input("enter distance in inches: "))
feet_m=feet*0.3048
feet_cm=feet*30.48
print(f'feet convert in meter is {feet_m} and in centimeter is {feet_cm}')
inch_m=inch*0.0254
inch_cm=inch*5.08
print(f'inch convert into meter is {inch_m} and in centimeter is {inch_cm}')

