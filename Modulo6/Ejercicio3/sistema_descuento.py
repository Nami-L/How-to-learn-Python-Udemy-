
print('*** Sistema de Descuentos***')

total_compra= int (input('Cuál fue el monto de tu compra? '))
miembro_tienda = input ('Eres miembro de la tienda(si/no)? ').strip().lower()


if total_compra > 1000 and miembro_tienda == 'si':
    descuento_10 = total_compra *.10
    total_a_pagar = total_compra - descuento_10
    print('Felicidades, has obtenido un descuento del 10%')
    print(f'Monto de la compra: ${total_compra:.2f}')
    print(f'Monto del descuento: ${descuento_10:.2f}')
    print(f'Monto final de la compra con descuento: ${total_a_pagar:.2f}')
elif miembro_tienda == 'si':
    duscuento_5 = total_compra *.05
    total_a_pagar = total_compra - duscuento_5
    print('Felicidades, has obtenido un descuento del 5%')
    print(f'Monto de la compra: ${total_compra:.2f}')
    print(f'Monto del descuento: ${duscuento_5:.2f}')
    print(f'Monto final de la compra con descuento: ${total_a_pagar:.2f}')
else:
    print('No obtuviste ningún tipo de descuento \nTe invitamos a hacerte miembro de la tienda')
    print(f'Monto final de la compra: ${total_compra:.2f}')