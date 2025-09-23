
print ('*** Creación de password ***')


password = input ('Ingresa un password(debe tener al menos 6 caracteres): ')

while len(password ) < 6:
    print('El pasword no cumple con los requisitos')
    password = input('Ingrese un nuevo valor de password: ' )
else:
    print('El valor de password es valido')