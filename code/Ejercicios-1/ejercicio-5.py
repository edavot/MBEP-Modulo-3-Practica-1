es_numerico = False

while not es_numerico:
    numero = input('Ingresa un número: ')
    es_numerico = numero.isnumeric()

mod = int(numero) % 2 

if mod == 0:
    print("El número es par")
else:
    print("El número es impar")