'''
Lists - like 'vectors' in R (1-dimensional data)
    "Grocery list" 
    Ordered in 1 direction
    
    Lists are made of 'items' or 'elements' (pieces of data)
        these items have POSITIONS in the list (indices)

    created with hard brackets (square brackets)

'''

grocery_list = ['peanut butter', 'bananas', 'chocolate', 'carrots']
num_list = [3.4, 5, -7.8]

print(grocery_list)
print(type(grocery_list))
print(type(num_list))

'''
All items have positions in the lists, represented numerically

In python, list indexing STARTS at 0
'''

print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[-2])


# Adding and removing items from lists

# Adding: .append()

grocery_list.append('pizza')
grocery_list.append('brussel sprouts')
grocery_list.append(True)
grocery_list.append(6.2)
print(grocery_list)


# Removing items from lists with .remove()

grocery_list.remove(True)
grocery_list.remove(6.2)


# SLICING: up to but not including
# range of items in a list
print(grocery_list[1:3])


# Logic with a list - sometimes more difficult in python
num_list = [3.4, 5, -7.8]
