# Proyecto Final

nombre= input('Ingresa sus nombres:')
apellidos= input ('Ingrese sus apellidos:')
empresa = input ('Ingrese el nombre de su empresa:')
extension_dominio= input ('Ingrese la extension de su dominio (.com, .es, .org):')

nombre = nombre.strip().lower().replace(' ','.')
#print(nombre)
apellidos = apellidos.strip().lower().replace(' ','.')
#print(apellidos)
empresa= empresa.strip().lower().replace(' ','')
email = ''.join ([nombre,'.' ,apellidos,'@',empresa,extension_dominio])
print (f'Su email es : {email}')