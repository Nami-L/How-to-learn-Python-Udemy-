# How to learn Python Udemy
Cursos de python proporcionado por UDEMY


## Variables de Entorno
 Las variables de entorno es que cuadno definimos una variable, almacena una referencia de memoria  y apunta a un objeto en un lugar de memoria


## Conversión de tipo de datos

La conversión de tipo de datos, tambien conocida como casting, es una técnica para manipular datos que no están en el tipo requerido
- convertir a entero **int**
- convertir a flotante **float**
- convertir a una cadena **str**
- convertir a un boleano **bool**

## Entrada de Datos por Consola

En python la entrada de datos se realiza usando la función input (). Esta función pausa la ejecución del programa and wait for  the user  enter some text from the keyboard. Then, when the user presses Enter, the text will be entered into  the console, return like a string

## Generar valores aleatorios
Function randint() is part of random modul, allow us to generate random numbers

## Operadores Lógicos
Se utilizan para realizar operaciones lógicas con valores booleanos.
- Operador lógico and 
- Operador lógico or
- Operador lógico negado

## Procedencia de Operadores en Pyton
## Resumen General

| Nivel Jerárquico        | Operadores                         |
|--------------------------|-------------------------------------|
| 1. Operador de paréntesis | ()                                |
| 2. Exponente             | **                                |
| 3. Unarios               | +x , -x                           |
| 4. Multiplicación, División, Módulo | *, /, //, %            |
| 5. Suma y Resta          | + , -                             |
| 6. Comparación           | ==, !=, <= , >=                   |
| 7. Operadores lógicos    | not, and, or                      |
| 8. Operadores de asignación | = , +=                         |

## Diagrama de Flujo

Un diagrama de flujo es una representación gráfica de los pasos a ejectgurar para lograr un resultado específico.
Se utilizand simbolos estandaraizados para represetnar distintos tipo de acciones.

- Óvalo: Representa el inicio o fin de un proceso.
- Rectángulo: Muestra instrucciones o acciones a ejecutar.
- Rombo: indica decisiones con múltiples flujos dependiendo si la respuesta es verdadera o falsa.
- Flechas : Dirigen el flujo del proceso, mostrando la dirección en que se mueven la secuencia de acciones.

![Diagrama de flujo](flujo.ong)

## Sentencia if elif else

La sentencia elif es una abreviatura de "else if", y se utiliza cuando necesitamos verificar múltiples condiciones, una tras otra.

## Operador Ternario

Es una forma compacta de agregar una condición y le objetivo es asignar un valor a una variable dependiendo del valor de la condición.

``` python
 resultado = valor_si_verdadero if condicion else valor_si_falso
```