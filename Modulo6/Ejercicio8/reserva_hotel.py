
print('*** Reserva de Hotel ***')

TARIFA_DIARIO_SIN_VISTA_MAR = 150.50
TARIFA_DIARIO_CON_VISTA_MAR = 190.50

nombre =input ('Nombre del Ciente: ')
dias_estadia = int (input ('Dias de Estadia: '))
vista_al_mar= input ('Con vista al mar (si/no)? ').strip().lower()
vista_al_mar_txt = vista_al_mar =='si'

if vista_al_mar_txt:
    costo_con_vista= dias_estadia * TARIFA_DIARIO_CON_VISTA_MAR
   # print(f'Cliente: {nombre}')
   # print(f'Días de Estadía: {dias_estadia}')
   # print(f'Costo total: {costo_con_vista}')
   # print(f'Habitación con vista al mar: {'Si' if vista_al_mar_txt else 'No'}')
else:
    costo_sin_vista= dias_estadia * TARIFA_DIARIO_SIN_VISTA_MAR
    
    
    
print(f'Cliente: {nombre}')
print(f'Días de Estadía: {dias_estadia}')
print(f'Costo total: {costo_sin_vista}')
print(f'Habitación con vista al mar: {'Si' if vista_al_mar_txt else 'No'}')