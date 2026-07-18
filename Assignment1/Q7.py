#Q7) Program to Find the Roots of a Quadratic Equation
#suppose we have a quadratic equation x^2-5y+6
a=1
b=-5
c=6
#quadratic equation
#  x1=-b+sqrt(b^2-4*a*c)/2a
#  x2=-b-sqrt(b^2-4*a*c)/2a
#  r=sqrt(b^2-4*a*c)
r=(((b**2)-4*a*c)**0.5)
print(r)
x1=((-b+r)/(2*a))
x2=((-b-r)/(2*a))
print(x1)
print(x2)
print(f"roots of quadratic equation is {x1} and {x2}")

