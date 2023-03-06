# Input five integers and display the maximum and the minimum numbers separately

five_int_numbers = list(input("Enter five integer numbers: "))

for i in five_int_numbers:
    print(i)
  
maximum = max(five_int_numbers)
minimum = min(five_int_numbers)

print(f"Maximum number is {maximum} and Minimum is {minimum}")

