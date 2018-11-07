"""This program calculates the area of circle, triangle and rectangle."""
from math import pi

print("The program is running :)")
option = input("Enter C for Circle or T for Triangle or R for Rectangle")

if option == 'C':
	radius = float(input("Enter radius :"))
	area = pi * radius**2
	print (("The area of circle: %f") % (area))

elif option == 'T':
	base = float(input("Enter base :"))
	height = float(input("Enter height :"))
	area = 0.5 * base * height
	print (("Area : %f") %(area))

elif option == 'R':
	width = float(input("Enter width :"))
	height = float(input("Enter height :"))
	area = width * height
	print (("Area : %f") %(area))

else:
	print("Error!! Invalid shape")


print("Exiting...")	
