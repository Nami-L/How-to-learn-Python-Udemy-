
print('*** Sentencia IF***')
edad= int (input('Introuduce tu edad: '))
#edad = 30
if edad >= 18:
    print(f'Eres mayor de edad y tu edad es: {edad} años')
elif 13 < edad < 18:
    print(f'Eres un adolescente y tu edad es: {edad} años')
else :
    print(f'Eres un niño y tu edad es: {edad} años  ')


print('Fin del programa')