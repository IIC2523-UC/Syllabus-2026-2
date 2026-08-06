# AC01 - Exclusion mutua con algoritmo del panadero

## Objetivo
En esta actividad vas a implementar el algoritmo del panadero de Lamport para resolver exclusion mutua entre multiples _threads_.

La idea es comparar dos escenarios:
- ejecucion sin sincronizacion (con condicion de carrera)
- ejecucion con algoritmo del panadero (sin lock de Python)

## Archivos entregados
- `main.py`: script base con experimento y una funcion incompleta

## Contexto funcional
El programa tiene un contador compartido `data[0]` que muchos _threads_ intentan incrementar.

Cada incremento separa lectura y escritura con pequenas pausas aleatorias para hacer visible la condicion de carrera.

Parametros del experimento:
- `CANTIDAD_THREADS`: cantidad de _threads_ concurrentes.
- `INCREMENTOS_POR_THREAD`: cuantas veces un _thread_ intenta incrementar el contador.
- `CANTIDAD_CORRIDAS`: cantidad de corridas para observar el comportamiento.

Valor esperado por corrida:
- `CANTIDAD_THREADS * INCREMENTOS_POR_THREAD`

## Tu tarea
Debes completar solo la funcion `algoritmo_panadero_lamport(thread_id)` en `main.py`.

Dentro de esa funcion implementa:
1. Fase de eleccion de ticket.
2. Espera activa respetando prioridad por `(numero, id_thread)`.
3. Entrada a seccion critica.
4. Salida de seccion critica.

No uses `threading.Lock` ni otras primitivas de exclusion mutua de la libreria estandar.

## Ejecucion esperada
Desde esta carpeta:

- `python3 main.py`

Salida esperada de forma conceptual:
1. En bloque `Sin sincronizacion`, el valor obtenido suele ser menor al esperado y puede variar entre corridas.
2. En bloque `Con algoritmo del panadero de Lamport`, el valor obtenido debe coincidir con el esperado en todas las corridas.

## Preguntas de reflexion
Responde brevemente:
1. ¿Qué problema corrige el algoritmo del panadero respecto a la version sin sincronizacion?
2. ¿Para qué sirve la variable `eligiendo` en el algoritmo?
3. ¿Cómo se rompe un empate cuando dos _threads_ tienen el mismo ticket?

## Entregable opcional
Sube un Zip con:
- `main.py` completo
- un archivo .md o .txt con respuestas de reflexión
