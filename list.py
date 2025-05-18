#list = used to store multiple items in a single variable

food = ["pizza", "hamburger", "hotdog", "spaghetti", "tacos"] #list of food items
print(food) #output: ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'tacos']
print(food[1]) #output: hamburger
print(food[1:3]) #output: ['hamburger', 'hotdog']
print(food[-1]) #output: tacos

food[0] = "sushi" #change the first item in the list
print(food) #output: ['sushi', 'hamburger', 'hotdog', 'spaghetti', 'tacos']
food.append("ice cream") #add an item to the end of the list
print(food) #output: ['sushi', 'hamburger', 'hotdog', 'spaghetti', 'tacos', 'ice cream']
food.remove("hamburger") #remove an item from the list
print(food) #output: ['sushi', 'hotdog', 'spaghetti', 'tacos', 'ice cream']
food.pop() #remove the last item from the list
print(food) #output: ['sushi', 'hotdog', 'spaghetti', 'tacos']

food.clear() #remove all items from the list
print(food) #output: []
food = ["pizza", "hamburger", "hotdog", "spaghetti", "tacos"] #list of food items
print(food) #output: ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'tacos']
food.sort() #sort the list in alphabetical order
print(food) #output: ['hamburger', 'hotdog', 'pizza', 'spaghetti', 'tacos']
food.reverse() #reverse the order of the list    
print(food) #output: ['tacos', 'spaghetti', 'pizza', 'hotdog', 'hamburger']   








