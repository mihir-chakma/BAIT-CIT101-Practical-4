"""
Input the length of the hypotenuse of an isosceles right-angled triangle and display the
length of a side rounded to two decimal places.
"""

import math

# taking input of the length of the hypotenuse
hypotenuse = float(input("Enter the length of the hypotenuse: "))

# calculating the length of a side using the hypotenuse of an isosceles right-angled triangle
side = math.sqrt((hypotenuse**2) / 2)

# displaying the length of the side rounded to two decimal places
print(f"Length of a side of the isosceles right-angled triangle is: {side:.2f}")
