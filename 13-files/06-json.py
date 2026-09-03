import json

user = {
    'nombre': 'Ricardo',
    'edad': 29,
    'active': True
}

with open('datos.json', 'w') as file:
    json.dump(user, file, indent=2)

with open('datos.json', 'r') as file:
    data_read = json.load(file)
    print(data_read)
