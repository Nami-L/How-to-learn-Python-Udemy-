
print ('*** Calculadora en Python ***')

valor_uno = valor_dos = 0
salir = False

while not salir:
    print (''' Operaciones que puedes realizar:
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir
           ''')
    opcion = int (input('Escoja una opción: '))
    if opcion == 1:
        valor_uno = int (input ('Dame el valor 1: '))
        valor_dos = int (input ('Dame el valor 2: '))
        suma= valor_uno + valor_dos
        print(f'El resultado de la suma es: {suma:.2f}')
    elif opcion == 2:
        valor_uno = int (input ('Dame el valor 1: '))
        valor_dos = int (input ('Dame el valor 2: '))
        resta= valor_uno - valor_dos
        print(f'El resultado de la resta es: {resta:.2f}')
    elif opcion == 3:
        valor_uno = int (input ('Dame el valor 1: '))
        valor_dos = int (input ('Dame el valor 2: '))
        multi= valor_uno * valor_dos
        print(f'El resultado de la resta es: {multi:.2f}')
    elif opcion == 4:
        valor_uno = int (input ('Dame el valor 1: '))
        valor_dos = int (input ('Dame el valor 2: '))
        divi= valor_uno / valor_dos
        print(f'El resultado de la resta es: {divi:.2f}')
    elif opcion == 5:
        salir =True
        print('Saliendo del programa de Calculadora. ¡Hasta pronto!\n')
    else:
        print('Opción inválida, proporciona otra opción ... \n')
else:
    print('Bye')
