# Input a finite, positive number and display its factorial

import math

# taking input of a finite, positive number
num = int(input("Enter a finite, positive number: "))

# calculating the factorial of the number using built-in function
factorial = math.factorial(num)

# displaying the factorial of the number
print("Factorial of", num, "is", factorial)
