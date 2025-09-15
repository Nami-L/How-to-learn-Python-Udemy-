# Calcular el are y perimetro de un rectangulo

altura = float (input ('Ingresa la altura del rectangulo: '))
base = float (input ('Ingresa la base del rectangulo: '))

area = altura * base
perimetro = 2 * (altura + base)

print(f'El area del rectangulo es : {area:.2f} y el perimetro del rectangulo es : {perimetro:.2f}')
