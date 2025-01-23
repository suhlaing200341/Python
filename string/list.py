# ==========list=============
list1 = ["abc", 34, True, 40, "male"]
print(len(list1))
print("the last item....", list1[len(list1) - 1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# ==============Change items value============
thislist[0] = "aa"
print("change items........", thislist)

thislist[1:3] = ["bb", "cc"]
print("change items 2........", thislist)

# ================append and extend==========
aa_list = [1, 2, 3]
aa_list.append(4)
print("append list......", aa_list)

bb_list = [5, 6, 7]
cc_dict = {"name": "Alex", "age": 21}
aa_list.extend(bb_list)
aa_list.extend(cc_dict)
print("extend list......", aa_list)

# ================remove items===========
cc_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cc_list.remove(3)
print("remove item.....", cc_list)

# ===========loop list==================
thislist = ["apple", "banana", "cherry", "orange"]
for item in thislist:
    print("for loop.....", item)

i = 0
while i < len(thislist):
    print(f"while loop....{i}", thislist[i])
    i += 1
    
# ==============short hand===============
short_hand_list = [item for item in thislist if not "a" in item]
print("short_hand_list.....", short_hand_list)

# ===============sort list================
sort_list = ["orange", "mango", "kiwi", "pineapple", "banana"]
sort_list.sort()
print("sort list.....", sort_list)

# ==============copy list==========
copy_list = sort_list.copy()
print("copy list....", copy_list)
print("counting.....", copy_list.count("mango"))