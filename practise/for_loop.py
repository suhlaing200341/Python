info_list = [
    {
        "name": "Alex",
        "age": "22",
    },
    {
        "name": "Eric",
        "age": "30",
    },
    {
        "name": "Laura",
        "age": "24",
    },
]
for item in info_list:
    age = item["age"]
    if item["name"] == "Eric":
        print(item)
    elif 22 < int(age) < 25:
        print(item)

for x in range(2, 6):
    if x == 4:
        break
    print(x)
    