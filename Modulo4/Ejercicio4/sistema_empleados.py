# Sistema empleado

print ('*** Sistema de Empleados ***')
nombre_empleado = input('Intruce el nombre del empleado : ')
edad_empleado = int (input('Introduce tu edad : '))
salario_empleado = float (input('Salario del empleado : '))
es_jefe_departament = input ('Es jefe de departamento (si/no) : ')

es_jefe_departament = es_jefe_departament.lower() == 'si'
print ('\n*** Datos del empleado ***')
print (f'Nombre del empleado : {nombre_empleado}')
print (f'Edad del empleado : {edad_empleado}')
print (f'Salario del empleado : {salario_empleado:.2f}')
print (f'Es jefe de departamento : {es_jefe_departament}')
