#for loops are used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects.
# while loops = unlimited 
# for loops = limited

import time

# for i in range(10): #range(10) = 0 to 9
#     print(i+1) #output: 1 to 10

# for i in range(50, 100+1, 2): #range(start, stop, step)
#     print(i)

# for i in "James Sanders":
#     print(i) #output: J a m e s   S a n d e r s

for seconds in range(10,0,-1): #countdown from 10 to 1
    print(seconds)
    time.sleep(1) #wait for 1 second
print("Happy New Year!") #output: Happy New Year!