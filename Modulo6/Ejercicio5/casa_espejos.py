
print('*** Bienvenido a la casa de los Espejos ***')

edad = int(input('Cual es tu edad?'))
tienes_miedo_oscuridad= input('Tienes miedo a la oscuridad (si/no)').strip().lower()=='si'

if not tienes_miedo_oscuridad and edad >= 10:
    print('Puedes entrar a los espenjos')
else:
    print('No puedes entrar a la casa de los espejos')