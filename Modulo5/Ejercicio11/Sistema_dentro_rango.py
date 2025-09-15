#Sistema de autenticacion

print('*** Sistema de valor dentro de Rango ***')
VALOR_MINIMO = 0
VALOR_MAXIMO = 5

dato = int(input('Ingresa un numero entre 0 y 5'))

dentro_del_rango = VALOR_MINIMO <= dato <= VALOR_MAXIMO

print(f'El valor {dato}esta dentro del rango? : {dentro_del_rango}')
