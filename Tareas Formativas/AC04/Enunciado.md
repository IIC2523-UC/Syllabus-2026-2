# AC04 - Eleccion de Lider con Raft

## Objetivo
En esta actividad vas a simular la fase de eleccion de lider del algoritmo Raft.

Dado un conjunto de nodos, cada uno con su log, su term y su election timeout, debes determinar cual (si es que alguno) se convierte en lider tras una unica ronda de votacion.

## Archivos entregados
En esta carpeta tienes:
- `main.py`: esqueleto principal para recorrer tests y mostrar resultados.
- `parser_tests.py`: script base para leer TXT y convertirlos a una estructura simple.
- `tests/`: ejemplos de archivos `.txt` para probar la solucion.

## Contexto funcional
Cada test tiene este formato:

1. Primera linea: IDs de nodos separados por coma.
- Ejemplo: `N1,N2,N3,N4`

2. Una linea por nodo, con el formato:
- `nodo;term;timeout;log`
- Ejemplo: `N1;2;150;A1-1,A2-1,A3-2`
- Significa: el nodo `N1` tiene actualmente `term=2`, `election timeout=150`, y su log tiene tres registros: `A1` (registrada en term 1), `A2` (term 1) y `A3` (term 2).
- Si el nodo no tiene logs, la parte de log queda vacia. Ejemplo: `N4;0;210;`
- Se garantiza que cada nodo tiene `election timeout` distinto.

El parser ya transforma cada test a una estructura simple con:
- `nodos`: lista de IDs.
- `info_nodos`: diccionario donde cada key es un nodo y el valor es un dict con `term` (int), `timeout` (int) y `log` (lista de dicts con `accion` y `term`).

Se simula una unica ronda de eleccion (un solo candidato, sin reintentos).

## Tu tarea
Debes completar `main.py` para:

1. Implementar `determinar_lider(caso)` usando las reglas de eleccion de lider de Raft vistas en clase (election timeout, term y comparacion de logs).
2. Procesar un unico test dado por ruta.
3. Imprimir quien es el candidato, el resultado de la votacion de cada nodo, y si finalmente gano o no la eleccion en esa unica ronda.

## Ejecucion esperada
Desde esta carpeta:

- `python3 main.py <ruta_test>`

Por ejemplo:

- `python3 main.py tests/test_01.txt`

## Preguntas de reflexion
Responde brevemente:
1. ¿Por qué un _election timeout_ aleatorio ayuda a que Raft funcione mejor?
2. ¿Por qué no basta con que un nodo tenga el _term_ mas alto para ganar la eleccion?
3. ¿Bajo que condicion un nodo con log vacio podria convertirse en lider?

## Entregable
Sube un Zip con:
- `main.py` completo
- un archivo .md o .txt con respuestas de reflexion
- (Opcional) tests extra creados por ti para probar tu implementacion
