def divide_numbers():
    try:
        a = int(input('Ingresa el numerador\n> '))  # a / b
        b = int(input('Ingresa el denominador\n> '))
        result = a / b
    except ValueError:
        print('Por favor, ingresa solo números.')
    except ZeroDivisionError:
        print('No se puede dividir entre cero.')
    except Exception as error:
        print(type(error))
    else:
        print(result)
    finally:
        print('Gracias por usar nuestra calculadora')


divide_numbers()
# else

# finally
