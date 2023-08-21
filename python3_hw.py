import math

def square_footage():
    width = int(input("What is the width of the home? "))
    length = int(input("What is the length of the home? "))
    area = length * width
    print(f"The area of this home is {area} square feet.")

def circumference():
    radius = int(input("What is the radius of the circle? "))
    circ = (2 * math.pi * radius)
    print(f"The circumference of this circle is {circ}")




