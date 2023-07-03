add = True
list_answers = ['SI', 'S', 'Y', 'YES']
list_names = []

while add:
    name = input('Ingresa un nombre: ')
    list_names.append(name)
    answer = input('¿Deseas agregar mas nombres? (Si/No)').upper()

    if answer not in list_answers:
        add = False
        
occurrence = {item: list_names.count(item) for item in list_names}

print(occurrence)