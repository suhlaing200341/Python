# ===========JSON===============
import json

json_str = '{"id": 1, "name": "Alex", "age": 21}'
python_dict = json.loads(json_str)
print("converting json to python......", python_dict)

py_dict = {"id": 1, "name": "Alex", "age": 21}
json_stri = json.dumps(py_dict)
print("converting python to json......", json_stri)