print('*** Aplicación de Salud y Fitness ***')

META_PASOS_DIARIO = 10000
CALORIAS_PASO_PASO = 0.04

# Pedimos los valores al usuario
nombre_usuario = input('Cual es tu nombre? ')
pasos_diarios = int(input('Cuántos pasos has caminado hoy? '))

# Verificar si el usuario alcanzó la meta de pasos diarios
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIO
meta_alcanzada_txt = 'si' if meta_alcanzada else 'no'

#Calculamos las calorias quemadas
calorias_quemadas= pasos_diarios * CALORIAS_PASO_PASO

#Mostrar la informacion

print(f'\n Usuarios: {nombre_usuario}')
print(f'Pasos dados hoy:{pasos_diarios}')
print(f'Calorías quemada: {calorias_quemadas}')
print(f'Meta de pasos diarios alcanzada: {meta_alcanzada_txt}')
print(f'La meta de pasos diarios es de : {META_PASOS_DIARIO}')

