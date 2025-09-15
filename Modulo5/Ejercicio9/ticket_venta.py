print('*** Generación de Ticket de venta ***')

precio_leche = float(input('Precio leche: '))
precio_pan = float(input('Precio pan: '))
precio_lechuga = float(input('Precio lechuga: '))
precio_platanos = float(input('Precio platanos: '))

descuento_porcentaja = int (input ('Cual es el decuesnto en porcentaje '))
#Calculo subtotal sin impuestao
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platanos

#calculo de impeusto 
impuesto = subtotal * 0.16

#calculo total de la compra con impuesto
costo_total = subtotal + impuesto

costo_descuento = costo_total * (descuento_porcentaja / 100)
costo_con_descuento = costo_total - costo_descuento

print(f'''' 
    subtotal: {subtotal:.2f}
    Impuesto: {impuesto:.2f}
    ----------------
    Total: {costo_total:.2f}
    Descuento : {costo_descuento} (%{descuento_porcentaja})
    ----------------
    Total con descuento: {costo_con_descuento:.2f}
      ''')