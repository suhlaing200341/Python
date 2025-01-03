# ===========Positive Slicing=============
text = "Hello, World!"
print("positive slicing....", text[2:5]) #0 is startindex, 5 is endindex
print("positive slicing....", text[:5]) # if not startindex, start 0
print("positive slicing....", text[7:]) # if not endindex, all the way to the end

# ==============Negative===========
print("negative slicing....", text[-5:-2])