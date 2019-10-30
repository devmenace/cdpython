import json

#   Sample JSON
userJSON = '{"first_name": "Den","last_name": "Ace","age": 18,"demouser": "demo","demopass": "demo"}'

#   Parse to dictionary
user = json.loads(userJSON)

print(f'{user} \n')

print(user['first_name'])

project = {'host': 'localhost', 'name': 'cdpython', 'author': 'Deniss Azema'}

projectData = json.dumps(project)

print(projectData)