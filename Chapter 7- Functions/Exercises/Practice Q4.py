# 4. Python program to calculate the area of a circle using a function
import math

def calculate_circle_area(radius):
    return math.pi * radius**2

# Example usage:
circle_radius = 5
area = calculate_circle_area(circle_radius)
print(f"The area of a circle with radius {circle_radius} is: {area}")
