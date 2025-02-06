class PersonalInfo:
    def __init__(self, info_list):
        self.info_list = info_list
        
    def __str__(self):
        return f"{self.info_list}"
    
    
info_list = [
    {"id": 1, "name": "Alex", "age": 21},
    {"id": 2, "name": "Eric", "age": 21},
    {"id": 3, "name": "Khara", "age": 24},
    {"id": 4, "name": "Emily", "age": 27},
    {"id": 5, "name": "Rose", "age": 26},
]
personal_info = PersonalInfo(info_list=info_list)

print("info_list...", personal_info)
