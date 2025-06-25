                                                                    ##############################
                                                                    ## Convertion of Data Types ##
                                                                    ##############################

# Converting Data Types in Python is a process of changing one data type to another.
# This can be done using built-in functions like int(), float(), str(), and bool().
# The conversion is often necessary when performing operations that require specific data types.
# For example, converting a string to an integer before performing arithmetic operations, or converting an integer to a string for concatenation.
    #concatenation is the process of joining two or more strings together.
    #For example, if you have a string "Hello" and an integer 5, you cannot concatenate them directly.
    #You need to convert the integer to a string first using str(5), then you can concatenate them like this: "Hello" + str(5).
    #The output will be "Hello5".
# Note that you cannot concatenate a string with an integer directly, as it will raise a TypeError.
# The operation of concatenation is only applicable to strings.

                                    #This code snippet demonstrates how to convert between different data types in Python.#

# Converting a string to an integer
print(int("123" + "456"))  # Converts the string "123" +"456" to the integer "123456"

# Converting a string to a float
print(float("123.45"))  # Converts the string "123.45" to the float 123.45

# Converting an integer to a string
print(str(123 + 456))  # Converts the integer 123 + 456 to the string "579"

# Converting a float to a string
print(str(123.45))  # Converts the float 123.45 to the string "123.45"

# Converting a boolean to a string
print(str(True))  # Converts the boolean True to the string "True"

# Converting a string to a boolean
print(bool("Hello"))  # Converts the non-empty string "Hello" to True
print(bool(""))  # Converts the empty string to False

# Converting an integer to a boolean
print(bool(1))  # Converts the integer 1 to True
print(bool(0))  # Converts the integer 0 to False

# Converting a float to a boolean
print(bool(1.23))  # Converts the float 3.14 to True
print(bool(0.0))  # Converts the float 0.0 to False

# Converting a boolean to an integer
print(int(True))  # Converts the boolean True to the integer 1
print(int(False))  # Converts the boolean False to the integer 0

# Converting a boolean to a float
print(float(True))  # Converts the boolean True to the float 1.0
print(float(False))  # Converts the boolean False to the float 0.0