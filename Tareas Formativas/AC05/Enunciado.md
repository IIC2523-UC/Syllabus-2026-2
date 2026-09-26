**# AC05 - Validación *Forward* en Control de Concurrencia**

**## Objetivo**

En esta actividad vas a simular la validación optimista del tipo *forward* para transacciones concurrentes.

Dado un historial de operaciones, debes decidir si cada transacción logra hacer `COMMIT` o si debe abortar.

**## Archivos entregados**

En esta carpeta tienes:

* `main.py`: esqueleto principal para recorrer tests y mostrar resultados.
* `parser_tests.py`: script base para leer TXT y convertirlo en una estructura simple.
* `tests/`: ejemplos de historiales para probar la solución.

**## Formato de los tests**

La primera línea contiene los IDs de las transacciones separados por coma:

`T1,T2,T3`

Cada línea siguiente representa una operación y tiene uno de estos formatos:

* `T1;BEGIN`
* `T1;READ;X`
* `T1;WRITE;X`
* `T1;COMMIT`

Las operaciones aparecen en el orden global en que ocurren. `VARIABLE` es un nombre sin espacios.

Se garantiza que:

* Cada transacción hace `BEGIN` antes de sus otras operaciones.
* Una transacción hace como máximo un `COMMIT` y posteriormente no hace ninguna otra operación.
* Las operaciones pertenecen a transacciones declaradas en la primera línea.

**## Validación *Forward***

Cuando una transacción `Ti` intenta hacer `COMMIT`, aplicará validación *forward* para determinar si puede o no hacer `COMMIT`. Para esta actividad, se asumirá que, si la validación indica que no se puede hacer `COMMIT`, entonces va a abortar inmediatamente.

Una transacción abortada deja de ser considerada activa y todas sus lecturas y escrituras dejan de aplicar.

**## Tu tarea**

Completa `main.py` para:

1. Procesar un historial desde una ruta recibida por argumento.
2. Registrar las lecturas y escrituras de cada transacción.
3. Implementar `validar_commit(transaccion, transacciones_activas)` usando validación *forward*.
4. Procesar los `COMMIT` en el orden del historial.
5. Devolver un diccionario que indique, para cada transacción, si pudo hacer `COMMIT` o si abortó.

La función `evaluar_caso(caso)` debe devolver solamente un diccionario con esta forma:

```python
{
    "T1": "COMMIT",
    "T2": "ABORT"
}
```

**## Ejecución esperada**

Desde esta carpeta:

`python3 main.py tests/test_01.txt`

**## Preguntas de reflexión**

Responde brevemente:

1. ¿Por qué la validación se hace al momento de `COMMIT` y no necesariamente al hacer `READ` o `WRITE`?
2. ¿Qué significa que una transacción activa lea una variable escrita por la transacción que intenta confirmar?
3. ¿Por qué una transacción abortada no debe dejar aplicadas sus escrituras?
4. ¿Por qué el resultado puede depender del orden de los `COMMIT`?

**## Entregable**

Sube un ZIP con:

* `main.py` completo;
* un archivo `.md` o `.txt` con las respuestas de reflexión;
* (opcional) tests extra creados por ti.
