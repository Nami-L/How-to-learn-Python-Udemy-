

print('*** Sistema de prestamode de Libros***')

tiene_credencia = input('Tienes credencial de estudiante(Si/No)? ').strip().lower()
DISTANCIA_PERMITIDA_KM = 3

distancia_biblioteca_km = int(input('Cuantos kilometros vives de la biblioteca? '))

es_elegible_prestamo = tiene_credencia == "si" or distancia_biblioteca_km < DISTANCIA_PERMITIDA_KM  
print(f'Eres elegible para el prestamo de libros: {es_elegible_prestamo} ')