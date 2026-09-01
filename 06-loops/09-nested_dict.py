nested_dict = {
    'Persona1': {
        'Nombre': 'Ricardo',
        'Edad': 29,
        'Ciudad': 'Ciudad de México'
    },
    'Persona2': {
        'Nombre': 'Brenda',
        'Edad': 26,
        'Ciudad': 'Huejutla de Reyes'
    },
    'Persona3': {
        'Nombre': 'Estela',
        'Edad': 50,
        'Ciudad': 'Cancún'
    }
}

for key, value in nested_dict.items():
    print(f'{key}:')
    for sub_key, sub_value in value.items():
        print(f'\t{sub_key}: {sub_value}')
