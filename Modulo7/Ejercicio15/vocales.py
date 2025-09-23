cadena = 'Hola Mundo'

vocal =0
for letra in cadena:
    if letra in 'aeiou':
        vocal += 1

print(f'Total de vocales encontrada :{vocal}')
