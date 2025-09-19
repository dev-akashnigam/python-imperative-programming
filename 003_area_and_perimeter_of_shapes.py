import math

print("Please enter the radius of circle: ")
radius_of_circle = float(input())

print("Please enter the length of rectangle: ")
length_of_rectangle = float(input())

print("Please enter the width of rectangle: ")
width_of_rectangle = float(input())

print("Please enter the length of first side of triangle: ")
first_side_of_triangle = float(input())

print("Please enter the length of second side of triangle: ")
second_side_of_triangle = float(input())

print("Please enter the length of third side of triangle: ")
third_side_of_triangle = float(input())

area_of_circle = math.pi * (radius_of_circle ** 2)
perimeter_of_circle = 2 * math.pi * radius_of_circle

area_of_rectangle = length_of_rectangle * width_of_rectangle
perimeter_of_rectangle = 2 * (length_of_rectangle + width_of_rectangle)

perimeter_of_triangle = first_side_of_triangle + second_side_of_triangle + third_side_of_triangle
semi_perimeter_of_triangle = perimeter_of_triangle / 2
area_of_triangle = math.sqrt(semi_perimeter_of_triangle * abs(semi_perimeter_of_triangle - first_side_of_triangle) * abs(semi_perimeter_of_triangle - second_side_of_triangle) * abs(semi_perimeter_of_triangle - third_side_of_triangle))

print(f"Area and Perimeter of Circle of radius: {radius_of_circle:.2f} = {area_of_circle:.2f}, {perimeter_of_circle:.2f}")
print(f"Area and Perimeter of Rectangle of length: {length_of_rectangle:.2f} and width: {width_of_rectangle:.2f} = {area_of_rectangle:.2f}, {perimeter_of_rectangle:.2f}")
print(f"Area and Perimeter of Triangle with side having lengths: {first_side_of_triangle:.2f}, {second_side_of_triangle:.2f} and {third_side_of_triangle:.2f} = {area_of_triangle:.2f}, {perimeter_of_triangle:.2f}")



