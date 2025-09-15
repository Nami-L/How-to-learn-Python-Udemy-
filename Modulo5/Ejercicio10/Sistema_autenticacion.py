#Sistema de autenticacion

print('*** Sistema de Autenticacion ***')

# Definir usuario y contrasena correctos
USUARIO_VALIDO = 'admin'
CONTRASENA_VALIDA = 1234

usuario =  input('Cual es tu usuario? ').strip()
contrasena = int(input ('Cual es tu password? ')).strip()

datos_correctos = (usuario == USUARIO_VALIDO) and (contrasena == CONTRASENA_VALIDA) 

print(f'Datos correctos? {datos_correctos}')