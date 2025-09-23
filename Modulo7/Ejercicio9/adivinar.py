from random import randint
print ('*** Juego de Adivinanzas ***')

numero_secreto = randint(1,50)
intento = 0
adivinanza = None
INTENTOS_MAXIMOS = 5

while adivinanza != numero_secreto and intento < INTENTOS_MAXIMOS:
    adivinanza = int (input ('Adivina el numero secreto (0-50): '))
    
    if adivinanza < numero_secreto:
        print('El numero secreto es mayor')
    elif adivinanza > numero_secreto:
        print('El numero secreto es menor')
    intento += 1

if adivinanza == numero_secreto:
    print(f'Felicidades adivinaste el numero secreto {numero_secreto} en un total de intentos {intento}')
else:
    print('Agotaste tus intentos. El número secreto era', numero_secreto)