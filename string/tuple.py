fruits = ("apple", "orange", "papara")
print("len of tuple.....", len(fruits))

# if you want to use methods of list in tuple, the first to do is change tuple to list. and then, use methods of list.
fruit_list = list(fruits)
fruit_list.append("chocolate")
fruits = tuple(fruit_list)
print("fruit ....", fruits)