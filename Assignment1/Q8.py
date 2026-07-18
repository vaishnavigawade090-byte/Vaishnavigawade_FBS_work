#Q8)Write a program to convert days into years, weeks and days.
days= 1000
#convert days into years
year=days//365
print(year)
days=days%365
print(days)
weeks=days//7
print(weeks)
days=days%7
print(days)
print(f"year is {year},days is {days},weeks is {weeks},days is {days}")
