num_list = [2, 11, 12, 3, 4, 6, 8, 10, 9]

even_list = [item for item in num_list if item % 2 == 0]
print("even list...", even_list)

alphabet_list = ["q", "c", "b", "a", "e", "c"]
if "c" in alphabet_list:
    print("c is present")
else:
    print("c is not absent.")