# Eric Risher.
# 6/25/2024.
# P2 Lab 1.
# Python script to calculate the diameter, circumference, and area of a circle using radius input.
# import math module for pi and pow operations
import math

# ask the user for input in the form of the radius of a circle with float variable.
print("What is the radius of the circle? ", end='')
input_string = float(input())

# convert string from user input into float variable.
rad_in = float(input_string)

# calculate diameter
diameter_float = float(2 * rad_in)

# circumference of circle
circ_float = float( 2 * math.pi * rad_in)

# area of the circle
ar_float = float(math.pi * pow(rad_in,2))

# print output of calculations
print()
print(f'The diameter of the circle is {diameter_float:.1f}')
print()
print(f'The circumference of the circle is {circ_float:.2f}')
print()
print(f'The area of the circle is {ar_float:.3f}')

# halt so user can copy info
input('\n Press Enter to Exit')