# Input three integers and display their GCD (Greatest Common Divisor) 

import math

# take input from the user
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

# find the GCD using math.gcd()
gcd = math.gcd(math.gcd(a, b), c)

# print the GCD
print(f"The GCD of {a}, {b}, and {c} is {gcd}")
