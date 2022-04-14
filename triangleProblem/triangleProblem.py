# triangle problem
import math


def formula(a, b, c):
    return (a**2 == b**2 + c**2-2*b*c*math.cos(a)) and (b**2 == a**2 + c**2-2*a*c*math.cos(b)) and (c**2 == a**2 + b**2-2*a*b*math.cos(c))


a = math.ceil(float(input("Enter the first side: ")))
b = math.ceil(float(input("Enter the second side: ")))
c = math.ceil(float(input("Enter the third side: ")))
print(f"The triangle is {a}, {b}, {c}")
if formula(a, b, c):
    print("The triangle is valid")
else:
    print("The triangle is invalid")
