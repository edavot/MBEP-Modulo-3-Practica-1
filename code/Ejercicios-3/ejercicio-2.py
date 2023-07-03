def multiply(*args):
    result = 0
    for value in args:
        if str(value).isnumeric():
            result = float(value) if result == 0 else result
            result = result * float(value)

    return result

print(multiply(1,2,3,4,5))
