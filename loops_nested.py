#nested loops the inner loop will run for each iteration of the outer loop
#nested loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")

#nested loops
for i in range(rows): #outer loop
    for j in range(columns): #inner loop
        print(symbol, end=" ") #print the symbol without a newline
    print() #print a newline after each row
# The outer loop iterates over the number of rows, and for each row, the inner loop iterates over the number of columns.

#output:
# Enter the number of rows: 3
# Enter the number of columns: 5
# Enter the symbol to use: *
# * * * * * 
# * * * * *
# * * * * *
# The output will be a rectangle of symbols with the specified number of rows and columns.

