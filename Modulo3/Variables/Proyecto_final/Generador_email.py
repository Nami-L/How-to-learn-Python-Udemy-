# # GEnerador de Email

# nombre = 'Luis Enrique Namigtle Jimenez'
# empresa = 'Global Mentoring'
# dominio = 'com.mx'

# nombre_lower = nombre.lower()
# empresa_lower = empresa.lower()
# dominio_lower = dominio.lower()

# lista_nombre = nombre_lower.split() # Separa el nombre en una lista
# lista_empresa = empresa_lower.split()




# #print(nombre)
# #print(empresa)
# #print(dominio)
# #print(nombre_lower)
# #print(empresa_lower)
# #print(dominio_lower)
# #print(lista_nombre)
# #print(lista_empresa)

# email = ''.join([lista_nombre[0],'.',lista_nombre[1],'.',lista_nombre[2],'.',lista_nombre[3],
#                 '@', lista_empresa[0],lista_empresa[1],'.',dominio_lower] ) # la cadena vacia es para llamar al metodo join


# print('*** GENERADOR DE EMAIL***')
# print (f'Nombre Usuario: {nombre}')
# print(f'Nombre empresa: {empresa}')
# print(f'Extensión del dominio: {dominio}'
#       )
# print(f'Email final generado : {email}')

print('*** Generador de Email ***')
nombre = ' Ubaldo Acosta Soto'
print(f'Nombre usario: {nombre}')
nombre_usuario = nombre.strip()
#print (nombre_usuario)
nombre_usuario= nombre_usuario.lower()
#print(nombre_usuario)
nombre_usuario = nombre_usuario.replace(' ','.')
print(f'Nombre usario normalizado: {nombre_usuario}')

####nombre de la empresa
nombre_empresa= ' Global Mentoring'
print(f'Nomnbre Empresa : {nombre_empresa}')
nombre_empresa = nombre_empresa.strip()
nombre_empresa= nombre_empresa.lower()
nombre_empresa = nombre_empresa.replace(' ','')
dominio = ' com.mx'
dominio = dominio.strip()
print(f'Extensión del dominio : {dominio}')

email = ''.join([nombre_empresa,'.',dominio])
#oncatenacion2 = ''.join([cadena1,' ',cadena2]) # la cadena vacia es para llamar al metodo join
email_final = ''.join([nombre_usuario,'@',email])
print(f'Email final generado : {email_final} ')
