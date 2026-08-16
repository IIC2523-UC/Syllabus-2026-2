# AC02 - De API Flask a RPC

## Objetivo
En esta actividad vas a tomar una API HTTP escrita con Flask y la vas a transformar a una arquitectura RPC.

La idea es comparar ambos enfoques y entender que cambia en:
- el servidor
- el cliente
- los tipos de datos que puedes enviar y recibir

## Archivos entregados
En esta carpeta tienes:
- `API/servidor.py`: API Flask con _endpoints_ HTTP
- `API/cliente.py`: cliente HTTP que consume la API
- `RPC/servidor.py`: esqueleto inicial de servidor RPC que debes completar
- `RPC/cliente.py`: esqueleto inicial de cliente RPC que debes completar

## Contexto funcional
El sistema administra evaluaciones y notas de alumnos.

### Operaciones requeridas
1. Crear evaluacion
- Tipo: POST
- Entrada: nombre de evaluacion (ejemplo: `T1`, `T2`)
- Efecto: guarda la evaluacion en una lista de evaluaciones existentes
- Retorno esperado: `None`

2. Registrar nota
- Tipo: POST
- Entrada: evaluacion, alumno, nota
- Efecto: guarda la nota en una lista de notas
- Retorno esperado: cantidad de notas que ese alumno tiene registradas

3. Consultar nota especifica
- Tipo: GET
- Entrada: alumno, evaluacion
- Retorno: nota para ese alumno en esa evaluacion

4. Consultar notas de un alumno
- Tipo: GET
- Entrada: alumno
- Retorno: lista con tuplas `(evaluacion, nota)`

5. Consultar promedio de una evaluacion
- Tipo: GET
- Entrada: evaluacion
- Retorno: promedio de esa evaluacion

6. Consultar estadisticas avanzadas de una evaluacion
- Tipo: GET
- Entrada: evaluacion
- Retorno: diccionario con `mediana`, `quartil`, `minimo`, `maximo`

## Tu tarea
Usando como referencia la carpeta `API`, completa los archivos `RPC/servidor.py` y `RPC/cliente.py` para implementar una solucion RPC funcional donde cada _endpoint_ de la API sea un método de invocación remota para el RPC con los mismos tipos de entregada y salida (tendrás 6 métodos).

El cliente RPC debe permitir ejecutar una demostracion equivalente a la del cliente HTTP.

Para esta actividad debes usar `xmlrpc.server` y `xmlrpc.client` de la libreria estandar de Python. Puedes hacer los supuestos que estimes convenientes como incluir casos bordes, más métodos, etc.


## Ejecucion esperada
Version base HTTP:
1. Levantar servidor:
   - `python3 API/servidor.py <puerto>`
2. Ejecutar cliente:
   - `python3 API/cliente.py <puerto>`

Version RPC (tu solucion):
- Debe permitir una ejecucion equivalente, pero usando llamadas RPC en vez de _endpoints_.
- Ejemplo esperado:
   - `python3 RPC/servidor.py <puerto>`
   - `python3 RPC/cliente.py <puerto>`

## Preguntas de reflexion
Responde brevemente al final:
1. ¿Qué tipos de datos puedes enviar y recibir en RPC?
2. ¿Se usa la misma clase para levantar un servidor y para conectarse a uno?
3. ¿Puedes enviar distintos tipos de datos en una misma solicitud RPC o se genera error?
4. ¿Es diferente el cliente de la API vs el cliente del RPC?

## Entregable opcional
Sube un Zip que contenga:
- `RPC/servidor.py` completo
- `RPC/cliente.py`
- un archivo .md o .txt con respuestas de reflexión

