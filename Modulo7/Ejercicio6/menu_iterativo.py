
print ('*** Aplicación de Cajero Automático ***')

SALDO = 1000

salir = False

while not salir:
    print(''' Menú
    1. Consulta de saldo
    2. Retirar
    3. Depositar
    4. Salir       
    ''')
    opcion= int (input('Elije una opción: '))
    if opcion == 1:
        print(f'Tu saldo actual es: ${SALDO:.2f}')
    elif opcion == 2:
        retirar= int(input('Ingresa el monto a retirar: '))
        if retirar > SALDO:
            print(f'No cuentas con el saldo suficiente. Saldo actual {SALDO:.2f}')
        else:
            SALDO -= retirar # saldo = saldo -retirar
            print(f'Tu nuevo saldo es : ${SALDO:.2f}')    
    elif opcion ==3:
        depositar= int(input('Ingresa el monto a depositar: '))
        SALDO += depositar 
        print(f'Tu nuevo saldo es: ${SALDO:.2f}')
    elif opcion == 4:
        print('Saliendo del cajero automático. ¡Hasta pronto!')
        salir= True
    else:
        print('Opción inválida, proporciona otra opción ... \n')
else :
    print('Terminando el sistema de Cajer automático')       