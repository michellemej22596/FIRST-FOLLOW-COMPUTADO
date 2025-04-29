# FIRST-FOLLOW-COMPUTADO
Silvia Illescas y Michelle Mejia

Este proyecto implementa las funciones FIRST y FOLLOW para una gramática libre de contexto, como parte del curso de Diseño de Lenguajes.

## Video de Funcionamiento
https://youtu.be/qxyG07SrzSQ

---
## Objetivo

Calcular los conjuntos FIRST y FOLLOW a partir de una gramática ingresada en un archivo .txt. El propósito es entender el funcionamiento de estos algoritmos fundamentales en el análisis sintáctico, y construir una base para futuros proyectos como generadores de analizadores sintácticos.

---

## Estructura del Proyecto


FIRST-FOLLOW-COMPUTADO/
├── grammar.txt         # Archivo de entrada con la gramática
├── main.py             # Script principal
├── parser.py           # Función para cargar y procesar la gramática
├── algorithms.py       # Algoritmos de FIRST y FOLLOW
└── README.md           # Descripción del proyecto


---

## Formato de Entrada (grammar.txt)

Cada línea representa una producción de la forma:


NoTerminal → símbolo1 símbolo2 ... símboloN


- Usa ε o epsilon para representar la producción vacía.
- Se pueden usar múltiples producciones para un mismo símbolo no terminal.

*Ejemplo:*

E → E + T
E → T
T → T * F
T → F
F → ( E )
F → id


---

## Ejecución

1. Asegúrate de tener Python instalado.
2. Coloca tu gramática en grammar.txt.
3. Ejecuta el programa:

bash
python main.py


---

## Ejemplo de Salida


Gramática cargada:
E → E + T
E → T
T → T * F
T → F
F → ( E )
F → id

Conjuntos FIRST:
Primero(E) = {'(', 'id'}
Primero(T) = {'(', 'id'}
Primero(F) = {'(', 'id'}

Conjuntos FOLLOW:
Siguiente(E) = {'$', '+', ')'}
Siguiente(T) = {'$', '+', ')', '*'}
Siguiente(F) = {'$', '+', ')', '*'}


---
