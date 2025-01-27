fruits = {"apple", "orange"}
fruits.add("chocolate")
print("add........", fruits)

num = ["1", "2", "3"] #you can use {}, [], tuple
fruits.update(num)
print("update method......", fruits)

# =============Remove methods===============
fruits.remove("1")
print("remove method......", fruits)

fruits.discard("2")
print("discard method......", fruits)

fruits.pop()
print("pop method......", fruits)

fruits.clear()
print("clear method......", fruits)