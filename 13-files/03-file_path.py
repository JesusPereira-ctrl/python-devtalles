# Relative Path
with open('../Archivos/archivo.txt', mode='r') as my_file:
    print(my_file.readlines())

# Absolute Path
with open('/home/jesus/Documentos/python/Archivos/archivo.txt', mode='r') as my_file:
    print(my_file.readlines())
