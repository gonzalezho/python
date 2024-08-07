file_path = "people.txt"

# Abrir el archivo en modo lectura
with open(file_path, "r") as people:
    # Leer todo el contenido del archivo
    read_people = people.read()

# Imprimir el contenido del archivo
print(read_people)
