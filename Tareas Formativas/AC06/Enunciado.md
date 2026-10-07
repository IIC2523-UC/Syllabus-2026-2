# AC06 - Consistencia Centrada en el Cliente

## Objetivo

Dado un historial de lecturas y escrituras hechas por distintos clientes sobre distintas réplicas, debes determinar, para cada cliente, si se cumplen las siguientes propiedades:

* **Monotonic Reads** (requisito mínimo)
* **Read Your Writes** (requisito mínimo)
* **Monotonic Writes** (desafío opcional, no es requisito mínimo)
* **Writes Follow Reads** (desafío opcional, no es requisito mínimo)

## Archivos entregados

En esta carpeta tienes:

* `main.py`: esqueleto principal con las 4 funciones a completar (2 obligatorias, 2 bonus) y el flujo para imprimir resultados.
* `parser_tests.py`: script base para leer TXT y convertirlo a una estructura simple.
* `tests/`: ejemplos de archivos `.txt` para probar tu solución.

## Formato de los tests

1. Primera línea: IDs de réplicas separados por coma.

   * Ejemplo: `R1,R2`

2. Segunda línea: IDs de clientes separados por coma.

   * Ejemplo: `A,B,C`

3. Líneas siguientes: un evento por línea, en orden temporal.

   * Escritura: `réplica;cliente;W;variable;version_anterior;version_nueva`

     * Ejemplo: `R1;B;W;X;1;3` significa que en la réplica `R1`, el cliente `B` escribe la variable `X`, pasando de la versión `1` a la versión `3` (equivalente a la notación `W_B(X1→X3)` vista en clases).
     * Si es la primera escritura de esa variable, `version_anterior` es `0`.

   * Lectura: `réplica;cliente;R;variable;version`

     * Ejemplo: `R2;A;R;X;2` significa que en la réplica `R2`, el cliente `A` lee la variable `X` y obtiene la versión `2`.

El parser ya transforma cada test a una estructura simple con:

* `replicas`: lista de IDs de réplicas.
* `clientes`: lista de IDs de clientes.
* `eventos_ordenados`: lista de eventos en orden temporal, cada uno con `t`, `replica`, `cliente`, `tipo`, `variable`, `version` (versión leída en `R`, versión nueva en `W`), y `version_anterior` (solo presente en eventos `W`).

## Tu tarea

Debes completar en `main.py`:

1. `verificar_monotonic_reads(caso)` **(obligatorio)**: retorna un `dict` `{cliente: True/False}`.

2. `verificar_read_your_writes(caso)` **(obligatorio)**: retorna un `dict` `{cliente: True/False}`.

3. `verificar_monotonic_writes(caso)` **(bonus, opcional)**: si no la implementas, déjala tal como está (retornando el mensaje de "no implementado").

4. `verificar_writes_follow_reads(caso)` **(bonus, opcional)**: ídem, opcional.

**Importante:** para cada cliente y cada propiedad, se asume que la propiedad **se cumple (`True`) a menos que encuentres evidencia explícita de que falla** en el historial.

## Ejecución esperada

Desde esta carpeta:

`python3 main.py tests/test_01.txt`

## Preguntas de reflexión

Responde brevemente:

1. ¿Qué combinación de eventos hace que un cliente viole _Monotonic Reads_ pero no _Read Your Writes_?

2. ¿Cómo podrías implementar estas 2 garantías en un sistema real, en vez de solo analizar un historial ya registrado?

3. **(Si implementaste el bonus)** ¿En qué se diferencia _Monotonic Writes_ de _Read Your Writes_?

## Entregable

Sube un Zip con:

* `main.py` completo (al menos las 2 funciones obligatorias)
* un archivo `.md` o `.txt` con respuestas de reflexión
* (Opcional) tests extra creados por ti, y las 2 funciones bonus si las implementaste.
