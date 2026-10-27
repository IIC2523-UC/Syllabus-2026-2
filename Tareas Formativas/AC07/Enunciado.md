# AC07 - Cifrado, Hash y Firma Digital

## Objetivo

En esta actividad vas a implementar y comparar tres formas de procesar un mensaje:

* Cifrado simétrico.
* Cifrado asimétrico.
* Funciones hash y firma digital.

Al finalizar, podrás observar cómo cambia el tiempo de procesamiento según el método y el tamaño del mensaje.

## Archivos entregados

En esta carpeta tienes:

* `main.py`: esqueleto con tres pipelines por completar y una función que mide sus tiempos.
* `rsa.py`: implementación de RSA utilizada por el programa. No requiere instalar librerías adicionales.

Las funciones auxiliares de cifrado, descifrado, hash y firma ya están implementadas en `main.py`.

Los algoritmos entregados son demostraciones didácticas y no deben utilizarse para proteger información real.

## Tu tarea

Completa en `main.py` las siguientes funciones:

1. `pipeline_simetrico(mensaje, clave_simetrica)`: debe retornar un resultado idéntico al mensaje original.

2. `pipeline_asimetrico(mensaje, clave_publica, clave_privada)`: debe retornar un resultado idéntico al mensaje original.

3. `pipeline_hash(mensaje, clave_publica, clave_privada)`: debe retornar `True` cuando la verificación sea correcta y `False` en caso contrario.

Debes utilizar las funciones auxiliares disponibles en `main.py` para completar cada _pipeline_ según los conceptos vistos en clases.

## Claves y medición

La función `main()` genera las claves una sola vez y las entrega como argumentos a `medir_tiempos`. Esta función mide los tres pipelines para mensajes de 100, 1.000, 10.000, 100.000 y 1.000.000 bytes, y comprueba que los resultados sean correctos.

No uses las claves como variables globales ni las generes al importar el módulo. Completa los pipelines sin cambiar sus parámetros ni la función `medir_tiempos`.

## Ejecución

Desde esta carpeta, ejecuta:

`python3 main.py`

El programa imprimirá los tiempos de procesamiento para cada tamaño de mensaje.

## Preguntas de reflexión

Responde brevemente:

1. ¿Qué diferencia hay entre el cifrado simétrico y el asimétrico en la forma en que se usan las claves?
2. ¿Por qué el hash y la firma digital permiten verificar un mensaje, pero no recuperar su contenido original ni mantenerlo secreto?
3. Según tus mediciones, ¿qué método escala mejor al aumentar el tamaño del mensaje? Explica el resultado.

## Entregable

Sube un ZIP con:

* `main.py` completo;
* un archivo `.md` o `.txt` con las respuestas a las preguntas de reflexión.
