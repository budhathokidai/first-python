import math                       #import is used to import modulus here

def calculate_area(radius):
    return math.pi * radius * radius      #math.pi represents the value of pie

radius = int(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print("The area of the circle with radius", radius, "is:", area)
