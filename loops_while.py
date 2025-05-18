#while loop will execute a block of code as long as the condition is true
# avod creating an infinite loop

name = ""

while len(name) == 0:
    name = input("What is your name? ")
    # The while loop will continue to execute as long as the condition is true.
    # In this case, the condition is that the length of the name is equal to 0.
    # If the user enters a name, the length of the name will no longer be equal to 0, and the loop will stop executing.

print("Hello, " + name + "!") # Concatenation