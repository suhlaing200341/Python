personal_info = {
    "name": "Alex",
    "age": "30",
    "address": "US",
    "hobby": "Signing"
}
print("Access 1.....", personal_info["hobby"])
print("Access 2.....", personal_info.get("name"))

# =======add new item======
personal_info["gender"] = "Male"
print("add new item to dict....", personal_info)

# =======remove item=======
""" pop() for specific value
    popitem() for the last item
    del
    clear()
"""
personal_info.pop("gender")
personal_info.popitem()
# personal_info.clear()
print("removing......", personal_info)

# ===========loop==============
for item in personal_info.keys():
    print("key.....", item)
    
for item in personal_info.values():
    print("value..", item)
    
for key, value in personal_info.items():
    print("key and value...", key, value)