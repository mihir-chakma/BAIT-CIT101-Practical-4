"""
A pipe repairman uses adhesive tape to repair cracks in some cylindrical pipes of
different diameters. Write a program to calculate the length of the tape needed as he
enters the diameter and the number of turns to cover each pipe.
"""

import math

# taking input of the diameter and the number of turns to cover the pipe
diameter = float(input("Enter the diameter of the pipe in cm: "))
turns = int(input("Enter the number of turns to cover the pipe: "))

# calculating the length of the tape needed to repair the pipe
circumference = math.pi * diameter 
tape_length = circumference * turns

# displaying the length of the tape needed to repair the pipe
print("Length of tape needed to repair the pipe is: {:.2f} cm".format(tape_length))

print(f"Length of tape needed to repair the pipe is: {tape_length:.2f} cm")
