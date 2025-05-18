# 2D list is a list of lists

drinks = [
    "coffee",
    "tea",
    "water",
    "soda",
    "juice"
]

dinners = [
    "pizza",
    "hamburger",
    "hotdog",
    "spaghetti",
    "tacos"
]
desserts = [
    "ice cream",
    "cake",
    "cookies",
    "brownies",
    "pie"
]

food  = [drinks, dinners, desserts] #2D list
print(food) #output: [['coffee', 'tea', 'water', 'soda', 'juice'], ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'tacos'], ['ice cream', 'cake', 'cookies', 'brownies', 'pie']]

#using index to access the elements of the 2D list
#food[index of list][index of what is in the before mentioned list]
print(food[0]) #output: ['coffee', 'tea', 'water', 'soda', 'juice']
print(food[1]) #output: ['pizza', 'hamburger', 'hotdog', 'spaghetti', 'tacos']
print(food[2]) #output: ['ice cream', 'cake', 'cookies', 'brownies', 'pie']
print(food[0][0]) #output: coffee
print(food[1][0]) #output: pizza
print(food[2][0]) #output: ice cream
print(food[0][1]) #output: tea
print(food[1][1]) #output: hamburger
print(food[2][1]) #output: cake
print(food[0][2]) #output: water
print(food[1][2]) #output: hotdog
print(food[2][2]) #output: cookies


