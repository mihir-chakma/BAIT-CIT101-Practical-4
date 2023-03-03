# Input an uppercase letter and display its ASCII code. (E.g. 'A' -> 65) 

letter = input("Input an uppercase letter: ").upper()
ascii_code = ord(letter)
print(ascii_code)


# get ascii code to char 
ascii_character = int(input("Input an ASCII letter: "))
letter = chr(ascii_character)
print(letter)
