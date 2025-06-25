                                                                ####################################
                                                                ### Number Convertion & F-String ###
                                                                ####################################

# Number convertion in Python is the process of converting one data type to another, such as converting a string to an integer or a float.
# This is often necessary when performing arithmetic operations or when you need to manipulate data in a specific format.

# Shorthand operators in Python are used to perform operations and assign the result to a variable in a single step.
# There are several shorthand operators in Python, including:
# += (addition and assignment), -= (subtraction and assignment), *= (multiplication and assignment), /= (division and assignment), //= (floor division and assignment), %= (modulus and assignment), **= (exponentiation and assignment).

# The += operator is used to add a value to a variable and assign the result back to that variable.
# Example:
x = 5
x += 3  # This is equivalent to x = x + 3
print(x)  # Output: 8

# The -= operator is used to subtract a value from a variable and assign the result back to that variable.
# Example:
y = 10
y -= 2  # This is equivalent to y = y - 2  
print(y)  # Output: 8

# The *= operator is used to multiply a variable by a value and assign the result back to that variable.
# Example:
z = 4
z *= 2  # This is equivalent to z = z * 2
print(z)  # Output: 8

# The /= operator is used to divide a variable by a value and assign the result back to that variable.
# Example:
a = 16
a /= 2  # This is equivalent to a = a / 2
print(a)  # Output: 8.0

# The //= operator is used to perform floor division on a variable and assign the result back to that variable.
# Example:
b = 17
b //= 3  # This is equivalent to b = b // 3
print(b)  # Output: 5

# The %= operator is used to perform modulus operation on a variable and assign the result back to that variable.
# Example:
c = 10
c %= 3  # This is equivalent to c = c % 3
print(c)  # Output: 1

# The **= operator is used to raise a variable to the power of a value and assign the result back to that variable.
# Example:
d = 2
d **= 3  # This is equivalent to d = d ** 3
print(d)  # Output: 8

                                                ## F-Strings in Python ##

# F-strings, or formatted string literals, are a way to embed expressions inside string literals, using curly braces `{}`.
# They are prefixed with the letter `f` or `F` and allow for inline expressions to be evaluated at runtime.
# F-strings are a more readable and concise way to format strings compared to the older `.format()` method or the `%` operator.
    # Example of using f-strings:
name = "Alice" # A string variable
age = 30 # An integer variable
greeting = f"Hello, my name is {name} and I am {age} years old." # Using f-string to format the string
print(greeting)  # Output: Hello, my name is Alice and I am 30 years old.

# F-strings can also include expressions, not just variable names:
result = f"The sum of 2 and 3 is {2 + 3}."
print(result)  # Output: The sum of 2 and 3 is 5.

# F-strings can also format numbers, such as specifying the number of decimal places:
pi = 3.14159
formatted_pi = f"The value of pi is approximately {pi:.2f}."
print(formatted_pi)  # Output: The value of pi is approximately 3.14

# F-strings can also be used with dictionaries and lists:
data = {"name": "Bob", "age": 25}
formatted_data = f"Name: {data['name']}, Age: {data['age']}"
print(formatted_data)  # Output: Name: Bob, Age: 25

# F-strings are evaluated at runtime, which means they can access variables and expressions defined in the current scope.

# This makes them very powerful for dynamic string formatting.
# Example of using f-strings with a list:
numbers = [1, 2, 3, 4, 5]
formatted_numbers = f"The first three numbers are: {numbers[0]}, {numbers[1]}, and {numbers[2]}."
print(formatted_numbers)  # Output: The first three numbers are: 1, 2, and 3.