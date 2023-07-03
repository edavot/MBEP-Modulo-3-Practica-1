
def read_number(message) -> float:
    '''Solicita un número al usuario'''
    is_numeric = False

    while not is_numeric:
        number = input(message)
        is_numeric = number.isnumeric()
    
    return number

min = int(read_number('Ingresa el número mínimo: '))
max = int(read_number('Ingresa el número máximo: '))

list_number = []
number_range = range(min, max + 1)

for value in number_range:
    if value % 3 == 0:
        list_number.append(value)

print(f'Números divisibles entre 3 entre el rango de {min}-{max}', list_number)