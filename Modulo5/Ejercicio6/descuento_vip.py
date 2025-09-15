

print('*** Sistema Descuento VIP ***')
NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input('Cauntos productos compraster hoy? '))  
tiene_memebresia= input('Tienes la membresía de la tienda(Si/No)? ').lower()

es_elegible_descuento = (cantidad_productos > NO_PRODUCTOS_DESCUENTO) and (tiene_memebresia == 'si')
print(f'Tienes acceso al descuento: {es_elegible_descuento} ')