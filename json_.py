import json
person_string = "{'name': 'Ali', 'language': ['python', 'c#']}"
person_dict = {'name': 'Ali', 'language': ['python', 'c#']}

## JSON string to Dict
# result = json.loads(person_string)
# print(result)
# print(type(result))

# result=result["lannguage"]

# with open("person.json.py") as f:
#    data=json.load(f)
#    print(data["name"])
#    print(data["language"])

# person_dict={
#    "name":"Ali",
#    "language":["python","C#"]
# }

# result=json.dumps(person_dict)
# print(result)

# with open("person.json","w") as f:
#    json.dumps(person_dict,f)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)
