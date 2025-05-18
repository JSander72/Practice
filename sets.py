#set = collection of unique elements
# #sets are unordered, unindexed, and do not allow duplicates

utensils = {"fork", "spoon", "knife"} #set of utensils
dishes = {"plate", "bowl", "cup"} #set of dishes

# utensils.add("napkin") #add an item to the set
# utensils.remove("fork") #remove an item from the set
# utensils.clear() #remove all items from the set

# dishes.update(utensils) #add items from one set to another
# print(dishes) #output: {'bowl', 'cup', 'knife', 'spoon', 'plate'}
dinner_table = dishes.union(utensils) #combine two sets
print(dinner_table) #output: {'bowl', 'cup', 'knife', 'spoon', 'plate'}

for x in dinner_table:
    print(x) #output: bowl, cup, knife, spoon, plate

    