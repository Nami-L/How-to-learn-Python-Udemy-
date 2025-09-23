print ('*** Dibujar triángulo Simétrico ***')
 
filas = int (input('Proporciona el número de filas: '))

for file in range(1,filas+1):
    espacio_blanco = ' ' * (filas- file)
    asterisco = '*' * (2*file - 1)
    print(espacio_blanco + asterisco)
