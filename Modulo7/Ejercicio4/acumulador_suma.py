
print ('*** Suma Acumulativa ***')

# Sumar los prmeros 5 numeros usando while

MAXIMO = 5
numero = 1

acumulador_suma= 0

#Empezar a iterar

while numero <= MAXIMO:
    # Imprimir lo que se va a sumar

    print (f'Acumulador suma + numero ---> {acumulador_suma} + {numero}')
    acumulador_suma += numero # al cacumulador le sumas el valor anterior
    numero += 1
    print(f'Suma Parcial : {acumulador_suma}')

print(f'\n Resultado de la suma acumulada es {acumulador_suma   }')