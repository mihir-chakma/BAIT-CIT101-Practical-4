# Input three integers and display their LCM (Least Common Denominator)

import math

# taking input of three integers
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

# finding LCM of three integers using built-in functions
lcm_ab = (a*b) // math.gcd(a,b)
lcm_abc = (lcm_ab*c) // math.gcd(lcm_ab,c)

# displaying the LCM of three integers
print(f"LCM of {a}, {b} and {c} is {lcm_abc}")
