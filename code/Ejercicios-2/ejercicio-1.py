add = True
list_answers = ['SI', 'S', 'Y', 'YES']
list_names = []

while add:
    name = input('Ingresa un nombre: ')
    list_names.append(name)
    answer = input('¿Deseas agregar mas nombres? (Si/No)').upper()

    if answer not in list_answers:
        add = False

print(list_names)
print(set(list_names))
print(tuple(list_names)) 