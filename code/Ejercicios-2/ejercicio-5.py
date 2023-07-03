add = True
list_vowels = ['A', 'E', 'I', 'O', 'U']
letter = input('Ingresa una letra: ').upper()

if letter in list_vowels:
    print('Es una letra vocal')
else:
    print('No es una letra vocal')