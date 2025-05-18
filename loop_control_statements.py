#loop control statements
# Loop control statements are used to change the execution of a loop

# break = used to exit a loop
# continue = used to skip the current iteration of a loop
# pass = used to do nothing 

while True:
    name = input("Enter your name: ")
    if name != "":
        break
    print("Hello, " + name + "!") # Concatenation 
# The break statement is used to exit the loop when the user enters "stop".

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end=" ") # end=" " is used to print the output on the same line


#PASS # The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.
# It is a null operation; nothing happens when it executes.


