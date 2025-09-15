# Operadores de Asignacion
numero = 5

print('*** Operadoes de Asignacion***')
numero = 5

print(f'El valor de numero es : {numero}')

cadena = 'Saludos desde python'
print(f'El valor de cadena es : {cadena}')

# Asifnacion multiples

variable1, variable2, variable3 = 1, 5, 'Luis'
print(f'El valor de variable1 es : {variable1}, la variables2 es:  {variable2} y la variable3 es: {variable3}')

# Asignacion en cadena

a = b = c = 10
print(f'El valor de a es : {a}, el valor de b es: {b} y el valor de c es : {c}')

# Intercambio de valores de una variable sin usar una variable temporal

a,b = 5,1
print(f'El valor de a es : {a} y el valor de b es: {b}')
a,b = b,a

print(f'El valor de a es : {a} y el valor de b es: {b}')

# Recibir multiples valores de la entrada del usuario

nombre, apellido = input ('ingresa tu nombre y apellido separados por una coma:').split(',')
print(f'El nombre es :{nombre} y el apellido es : {apellido}')