# Manejo de subcadenas

cadena = 'Hola Mundo'

subcadena_hola = cadena[0:4] #En realidad es de 0 a 3 porque el ultimo indice no se incluye
print(f'subcadena hola:{subcadena_hola}')

subcadena_mundo = cadena[5:10] #En realidad es de 5 a 9 porque el ultimo indice no se incluye
print(f'subcadena mundo:{subcadena_mundo}')

## Encontrar el indice de una subcadena

indice = cadena.find('Mundo')
print(f'Indice de la sucadena mundo:{indice}')

# Reemplazar una subcadena

nueva_cadena = cadena.replace('Mundo','Python')
print(f'Nueva cadena es: {nueva_cadena}')

nueva_cadena2 = cadena.replace('Hola','Adios')
print(f'Nueva cadena es: {nueva_cadena2}')

# Seperadores split, divide una cadena en una lista de subcadenas
datos= 'Bienvenidos a Python'
lista = datos.split() # Sepera cada elemento cada que encuentra un espacio en blanco
print(lista)
datos = 'Bienvenidos,a,Python'
lista = datos.split(',') # Sepera cada elemento cada que encuentra una coma
print(lista)

# Multiplicacion de cadenas

texto = 'Hola '
veces= 3
resultado = texto * veces
print(resultado)