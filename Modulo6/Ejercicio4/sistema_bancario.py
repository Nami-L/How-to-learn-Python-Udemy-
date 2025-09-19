
print('*** Sistema Bancario ***')

salir_sistema = input('Deseas salir del sistema (si/no)? ').strip().lower()
salida_sistema = salir_sistema == 'si'


if not salida_sistema:
    print('Continuamos dentro del sistema')
else: 
    print('Salimos del sistema')
    

