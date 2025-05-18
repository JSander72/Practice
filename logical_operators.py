#logical operators
# Logical operators are used to combine conditional statements

#used to check if two or more conditions are true

temp = int(input("What is the temperture outside?: "))

if temp >= 0 and temp <= 30: # AND = logical operator: checks if both conditions are true
    print("The temperature is normal.")
    print("Go for a walk.")

elif not (temp >= 0 and temp <= 30): # NOT = logical operator: reverses the result of the condition
    print("The temperature is abnormal.")
    print("Stay indoors.")

elif temp < 0 or temp > 30: # OR = logical operator: checks if at least one condition is true
    print("The temperature is abnormal.")
    print("Stay indoors.")
    