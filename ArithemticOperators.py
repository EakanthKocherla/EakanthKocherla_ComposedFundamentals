                                                                     ############################
                                                                     ### Arithmetic Operators ###
                                                                     ############################

# Arithemtic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.
# In Python, these operators can be used with integers, floats, and even strings (for concatenation).
# The basic arithmetic operators in Python are:
# + (addition), - (subtraction), * (multiplication), / (division), // (floor division), % (modulus), and ** (exponentiation).

# This code snippet demonstrates the use of arithmetic operators in Python.

# Addition
print(5 + 3)  # Adds 5 and 3, output: 8

# Subtraction
print(10 - 2)  # Subtracts 2 from 10, output: 8

# Multiplication
print(4 * 2)  # Multiplies 4 and 2, output: 8

# Division
print(16 / 2)  # Divides 16 by 2, output: 8.0 
#even though 16 / 2 is an integer, the result is a float in Python. This is the default behavior in Python 3 called implicit type conversion.

# Floor Division
print(17 // 3)  # Floor divides 17 by 3, output: 5

# Exponentiation
print(2 ** 3)  # Raises 2 to the power of 3, output: 8

# Modulus
print(10 % 3)  # Returns the remainder of 10 divided by 3, output: 1

# Order of operations in Python follows the standard mathematical rules known as PEMDAS.
# PEMDAS stands for:
# PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)
# This means that operations inside parentheses are performed first, followed by exponents, then multiplication and division and finally addition and subtraction.
# The order of operations can be overridden by using parentheses to group operations.
# Execution is always from left to right, except for exponentiation which is right associative.
# Example of order of operations
print(2 + 3 * 4)  # Output: 14, because multiplication is performed before addition.
print((2 + 3) * 4)  # Output: 20, because parentheses override the order of operations.

# round() function is used to round a number to a specified number of decimal places.
# If no decimal places are specified, it rounds to the nearest integer.
print(round(3.14159, 2))  # Rounds 3.14159 to 2 decimal places, output: 3.14
print(round(3.14159))  # Rounds 3.14159 to the nearest integer, output: 3