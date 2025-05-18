#tuples = a collection of ordered and immutable elements
# #tuples are used to store multiple items in a single variable
# #tuples are similar to lists, but they cannot be changed or modified

student = ("John", 25, "male") #tuple of student information

print(student.count("John")) #output: 1
print(student.index("male")) #output: 2

for x in student:
    print(x) 

if "John" in student:
    print("Student is here") #output: Student is here