numero_base = 17
es_numerico = False

while not es_numerico:
    numero = input('Ingresa un número: ')
    es_numerico = numero.isnumeric()

resultado = 0
if float(numero) > numero_base:
    resultado = (numero_base * 2) - float(numero)
else:
    resultado = numero_base - float(numero)

print(resultado)
