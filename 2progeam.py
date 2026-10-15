#menu drivar program
from email.mime import base
from random import choice

print("----manu----")
print("1.Area of circle")
print("2.Area of triangle")
print("3.Area of square")
print("4.Area of rectangle")
print("5.Area of interest")
if choice==1:
    radius = float(input("Enter radius: "))
    area= 3,14*radius*radius
    print("The area of the circle is ",area)
elif choice==2:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area= 0.5*base*height
    print("The area of the triangle is ",area)
elif choice==3:
    side = float(input("Enter side: "))
    area= side*side
    print("The area of the square is ",area)

elif choice==4:
    length = float(input("Enter length: "))
    breath = float(input("Enter breath: "))
    area= length*breath
    print("The area of the rectangle is ",area)
elif choice==5:
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time of years: "))
    si = (principal*rate*time)/100
    print("simple interest is ",si)
else:
    print("Invalid choice")
