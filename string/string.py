# =========String are array=========
a = "Hello World!"
print("string are array", a[1])

# ===========String loop=======
fruit = "apple"
for item in fruit:
    print("String loop", item)
    
# =============String length===========
name = "Alex"
print("string length.....", len(name))

# ==========Check string==========
text = "it is a programming book."
book = "programming"
if book in text:
    print("check string......, it is present")
if book not in text:
    print("check string......, it is not present")