str = input('Ingresa un dato: ')

has_numbers = any(chr.isdigit() for chr in str)

if has_numbers:
    print('La cadena contiene números')
else:
    print('La cadena no contiene números')