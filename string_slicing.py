# slicing a string = create a substring by extracting elements form another string indexing[] or slice()
# #string[start:stop:step]
# #start = the index of the first character to include in the substring
# #stop = the index of the first character to exclude from the substring
# #step = the number of characters to skip between each character in the substring

#String Indexing[]
name = "James Sanders"

first_name = name[0:5] #substring 
print(first_name) #output: James

last_name = name[6:13] #substring
print(last_name) #output: Sanders

#substring = a part of a string
#slicing = extracting a substring from a string

#step
#name[start:stop:step]
funky_name = name[0:13:2] #substring step selects every second character
print(funky_name) #output: JmsSnes

reversed_name = name[::-1] #substring step selects every character in reverse order
print(reversed_name) #output: srednaS semaJ

#String Slicing()
website = "https://www.google.com"

slice = slice(11,-4)

website[slice] #substring
print(website[slice]) #output: google
