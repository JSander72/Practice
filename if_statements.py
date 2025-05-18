#if statements = conditional statements that execute a block of code if a condition is true

age = int(input("How old are you? "))
# The input function returns the data as a string, so we need to convert it to the appropriate type if necessary.


if age == 100:
    print("You are a century old.")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You havent been born yet.")
else:
    print("You are a child.")



# The if statement checks if the condition is true, and if it is, it executes the block of code inside the if statement.
# The else statement executes the block of code inside it if the condition is false.
