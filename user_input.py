name = input("What is your name? ")
#input is a built-in function that allows the user to enter data from the keyboard.
# The input function returns the data as a string, so we need to convert it to the appropriate type if necessary.

print("Hello, " +name + "!") # Concatenation
# The + operator is used to concatenate strings in Python.
# Concatenation is the process of joining two or more strings together.

age = input("How old are you? ")
# The input function returns the data as a string, so we need to convert it to the appropriate type if necessary.
# For example, if we want to accept an integer from the user, we can use the int function to convert the input to an integer.
age = int(age) #convert string to int
print("You are " + str(age) + " years old!") # Concatenation

#what if we need to accept a number from the user?
# We can use the input function to accept a number from the user, but we need to convert it to the appropriate type.

#float = input("Enter a float number: ")
height = float(input("How tall are you?: "))
print("You are " + str(height) + " cm tall!") # Concatenation



