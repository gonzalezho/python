# Read file
my_file = open("data.txt", "r")
file_content = my_file.read()
my_file.close()
print(file_content)

fido = "Fido Dido"
my_file_writing = open("data.txt", "w") # Writing in file
my_file_writing.write(fido)
my_file_writing.close()
