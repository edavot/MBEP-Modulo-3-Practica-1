def is_prime(number):
    result = False
    count = 0

    for value in range(2, number):
        if number % value == 0:
            count += 1

    if count == 0:
        print(number, 'Número primo')
    else:
        print(number, 'No es numero primo')

is_prime(7)
is_prime(14)