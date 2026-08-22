# AC03 - Reloj vectorial

## Objetivo
En esta actividad vas a implementar el algoritmo de reloj vectorial.

Dada una secuencia de eventos en archivos TXT, debes calcular el vector logico de cada evento para cada nodo.

## Archivos entregados
En esta carpeta tienes:
- `main.py`: esqueleto principal para recorrer tests y mostrar resultados
- `parser_tests.py`: script base para leer TXT y convertirlos a una estructura simple
- `tests/`: ejemplos de archivos `.txt` para probar la solucion
- `svg/`: diagramas visuales de los tests.

## Contexto funcional
Cada test tiene este formato:

1. Primera linea: IDs de nodos separados por coma.
- Ejemplo: `ID1,ID2,ID3`

2. Lineas de eventos locales:
- Ejemplo: `T1,ID1-A`
- Significa: en tiempo `T1` ocurre el evento `A` en nodo `ID1`.

3. Lineas de comunicacion:
- Ejemplo: `T3,ID1-B#T4,ID2-C`
- Significa: en `T3` ocurre un evento de envio (`B`) en `ID1` que gatilla un evento de recepcion (`C`) en `ID2` en `T4`.

El parser ya transforma cada test a una estructura simple con:
- `nodos`: lista de IDs
- `eventos_por_nodo`: diccionario donde cada key es un nodo y el valor es la lista de eventos de ese nodo
- `eventos_ordenados`: lista unidimensional de eventos para procesar por tiempo. Se recomienda realizar un `for` por ella y calcular el vector a cada evento según corresponde.


## Tu tarea
Debes completar `main.py` para:

1. Implementar `calcular_vector_logico(caso)` usando reglas de reloj vectorial.
2. Procesar un unico test dado por ruta.
3. Imprimir el vector logico de cada evento, en orden temporal.

Para los vectores, asume que cada componente respeta el mismo orden que la lista de nodos. Por ejemplo, si la lista es `["A", "B", "C"]`, entonces los vectores serán `[Componente A, Componente B, Componente C]`.

Asume que al empezar un tests, cada nodo tiene su vector con todas las componentes en 0.


## Ejecucion esperada
Desde esta carpeta:

- `python3 main.py <ruta_test>`

Por ejemplo:

- `python3 main.py tests/test_01.txt`

## Preguntas de reflexion
Responde brevemente:
1. ¿Qué informacion extra entrega un reloj vectorial respecto a los relojes de Lamport?
2. ¿Comé se detecta concurrencia entre dos eventos con vectores `V` y `W`?
3. ¿Qué costo tiene usar vectores cuando aumenta la cantidad de nodos?

## Entregable
Sube un Zip con:
- `main.py` completo
- un archivo .md o .txt con respuestas de reflexión
- (Opcional) tests extra creados por ti para probar tu implementacion
