# letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# números = '0123456789'
# símbolos = '!@#$%^&*()_+-=[]{}\;:,.<>?/'
# caracteres = letras + números + símbolos
# Formula simple: (item * 7 + 3) % len(caracteres)

# Entrada: 8
# Salida: &D^#23SN

import string
import random


def password_generator(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = []

    for _ in range(length):
        index = random.choice(chars)
        password.append(index)

    return ''.join(password)


length = int(input('¿Cuantos caracteres quieres en tu contraseña?\n> '))
print('Tu contraseña segura es:', password_generator(length))
