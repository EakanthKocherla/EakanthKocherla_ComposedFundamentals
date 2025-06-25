                                                                #######################
                                                                ## Checking the Type ##
                                                                #######################

                        # This script demonstrates the use of the len() function and checks the type of various objects in Python.

# Prints the length of the string. len is a built-in function that returns the number of items in an object. Does not work with integers.

print (len("123456")) 

#Checking the type of various objects.

print(type(len))  # Prints the type of the object. Prints <class 'builtin_function_or_method'> for built-in functions.
print(type(len("123456")))  # Prints the type of the object. Prints <class 'int'> for integer, since len returns an integer.

                        #########################################################################################
                        #Major Primitive data types in Python are strings, integers, floats, booleans, and None.#
                        #########################################################################################

#String is a sequence of characters enclosed in quotes, either single or double.
#Strings can be indexed and sliced, and they are immutable (cannot be changed after creation).
#String always goes with quotes, integers and floats do not.

print(type("Hello")) # Prints the type of the object. Prints <class 'str'> for string.

#Integer is a whole number, positive or negative, without decimals.
#Integers can be of any size, limited only by the memory available.

print(type(123))    # Prints the type of the object. Prints <class 'int'> for integer.

#Float is a number that has a decimal point or is in exponential form.
#Floats can represent real numbers and can also be of any size, limited by the memory available.

print(type(3.14))  # Prints the type of the object. Prints <class 'float'> for float.

#Boolean values are True and False, they are case-sensitive.

print(type(False)) # Prints the type of the object. Prints <class 'bool'> for boolean.
print(type(True))  # Prints the type of the object. Prints <class 'bool'> for boolean.

#None is a special constant in Python that represents the absence of a value or a null value.

print(type(None))  # Prints the type of the object. Prints <class 'NoneType'> for None.
