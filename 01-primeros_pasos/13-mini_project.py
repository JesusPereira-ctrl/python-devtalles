# Registro
# Recibas de forma dinámica el nombre, año de nacimiento, correo y contraseña

'''
    Nombre: Ricardo
    Email: ricardo@correo.com
    Tendrás 55 años en el 2050
    Tu contraseña es: ****
'''

name = input('¿Cual es tu nombre?\n> ')
year_of_birth = input('¿En que año naciste?\n> ')
email = input('¿Cual es tu correo electrónico?\n> ')
password = input('¿Escribe una contraseña?\n> ')

future_age = 2050 - int(year_of_birth)
password_length = len(password)

card = f'''
    Nombre: {name}
    Email: {email}
    Tendrás {future_age} años en el 2050
    Tu contraseña es: {'*' * password_length}
'''

print(card)
