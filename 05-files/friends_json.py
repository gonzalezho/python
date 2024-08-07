import json

# Leer el contenido de un archivo JSON
with open("friends_json.json", "r") as file:
    data = json.load(file)

print(data)
