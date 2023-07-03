def read_number() -> float:
    '''Solicita un número al usuario'''
    is_numeric = False

    while not is_numeric:
        number = input('Ingresa un número: ')
        is_numeric = number.isnumeric()
    
    return number
    
result = 0
number_1 = float(read_number())
number_2 = float(read_number())
number_3 = float(read_number())

result = number_1 + number_2 + number_3

if number_1 == number_2 and number_2 == number_3:
    result = result * 3

print(result)
