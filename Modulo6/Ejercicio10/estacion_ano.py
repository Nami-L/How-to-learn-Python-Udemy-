print('*** Identicación Estación de año ***')

mes = int (input('Escriba el nnumero  del mes (1-12): '))

if mes == 1 or mes ==2 or mes ==12:
    print(' Invierno')
elif mes==3 or mes== 4 or mes==5:
    print('Primavera')
elif mes == 7 or mes==6 or mes ==8:
    print('Verano')
elif mes == 9 or mes == 10 or mes== 11:
    print('Otoño')

else:
    print('Estacion desconocida')