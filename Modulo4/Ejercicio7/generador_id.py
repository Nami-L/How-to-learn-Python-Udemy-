#generador ID
from random import randint

print('*** Sistema Generador de ID Unico***')
nombre = input('Cual es tu Nombre?')
apellido = input ('Cual es tu Apellido?')
nacimiento= input('Cual es tu año de nacimiento (YYYY)?')
numero_random = randint(0,10000)
numero_random_str= str(numero_random)
two_letter_nombre = nombre.strip().upper()[0:2]
two_letter_apellido = apellido.strip().upper()[0:2]
two_numer_nacimiento = nacimiento.strip()[2:4]

identificador = ''.join([two_letter_nombre,two_letter_apellido,two_numer_nacimiento,numero_random_str])
print(f'Hola Juan, \n Tu nuevo número de identicación (ID) generador por el sistema es: \n {identificador} \n Felidicidades!')
print('_________________________________')