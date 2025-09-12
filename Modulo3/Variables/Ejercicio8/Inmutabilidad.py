
## Manejo de inmutabilidad de cadenas

cadena1 = 'Hola Mundo'
#cadena1[0] = 'h'  # Esto generará un error porque las cadenas son inmutables
cadena2= cadena1
print(cadena2)
cadena1= 'Adios'
print(cadena1)