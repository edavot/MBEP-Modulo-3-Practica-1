list_names = ['Francisco', 'Alberto', 'Rodrigo', 'Joana', 'Rebeca', 'Susana']
list_answers = ['SI', 'S', 'Y', 'YES']

answer = input('¿Deseas crear tu propia lista de nombres ?')

if answer in list_answers:

    add = True
    list_names = []

    while add:
        name = input('Ingresa un nombre: ')
        list_names.append(name)
        answer = input('¿Deseas agregar mas nombres? (Si/No)').upper()

        if answer not in list_answers:
            add = False

name = input('Ingresa un nombre: ')

if name in list_names:
    print('Nombre encontrado en la lista')
else:
    print('El nombre no se encontro en la lista')