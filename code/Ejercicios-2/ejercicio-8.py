is_numeric = False
milliseconds = 0

while not is_numeric:
    milliseconds = input('Ingresa los milisegundos: ')
    is_numeric = milliseconds.isnumeric()

milliseconds = int(milliseconds)
seconds = (milliseconds/1000)%60
seconds = int(seconds)
minutes=(milliseconds/(1000*60))%60
minutes = int(minutes)
hours=(milliseconds/(1000*60*60))%24
hours = int(hours)

print(seconds, minutes, hours)