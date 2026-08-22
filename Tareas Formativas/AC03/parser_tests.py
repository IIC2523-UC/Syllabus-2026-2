from pathlib import Path


def _parse_nodo_evento(texto: str) -> tuple[str, str]:
    nodo, evento = texto.split("-", maxsplit=1)
    return nodo.strip(), evento.strip()


def _parse_tiempo(texto: str) -> int:
    texto = texto.strip()
    if not texto.startswith("T"):
        raise ValueError(f"Tiempo invalido: {texto}")
    return int(texto[1:])


def parsear_test(ruta_test: str) -> dict:
    ruta = Path(ruta_test)
    lineas = [linea.strip() for linea in ruta.read_text(encoding="utf-8").splitlines() if linea.strip()]

    if not lineas:
        raise ValueError(f"Archivo vacio: {ruta_test}")

    nodos = [nodo.strip() for nodo in lineas[0].split(",") if nodo.strip()]
    eventos_por_nodo = {nodo: [] for nodo in nodos}
    eventos_ordenados = []

    contador_mensajes = 1

    for linea in lineas[1:]:
        if "#" in linea:
            parte_envio, parte_recepcion = linea.split("#", maxsplit=1)

            tiempo_envio_txt, envio_txt = [p.strip() for p in parte_envio.split(",", maxsplit=1)]
            tiempo_recepcion_txt, recepcion_txt = [p.strip() for p in parte_recepcion.split(",", maxsplit=1)]

            nodo_envio, evento_envio = _parse_nodo_evento(envio_txt)
            nodo_recepcion, evento_recepcion = _parse_nodo_evento(recepcion_txt)

            tiempo_envio = _parse_tiempo(tiempo_envio_txt)
            tiempo_recepcion = _parse_tiempo(tiempo_recepcion_txt)

            mensaje_id = f"m{contador_mensajes}"
            contador_mensajes += 1

            eventos_por_nodo[nodo_envio].append(
                ("envia", tiempo_envio, evento_envio, nodo_recepcion, tiempo_recepcion, evento_recepcion)
            )
            eventos_por_nodo[nodo_recepcion].append(
                ("recibe", tiempo_recepcion, evento_recepcion, nodo_envio, tiempo_envio, evento_envio)
            )

            eventos_ordenados.append(
                {
                    "tipo": "send",
                    "t": tiempo_envio,
                    "nodo": nodo_envio,
                    "evento": evento_envio,
                    "msg": mensaje_id,
                    "to": nodo_recepcion,
                    "to_evento": evento_recepcion,
                }
            )
            eventos_ordenados.append(
                {
                    "tipo": "recv",
                    "t": tiempo_recepcion,
                    "nodo": nodo_recepcion,
                    "evento": evento_recepcion,
                    "msg": mensaje_id,
                    "from": nodo_envio,
                    "from_evento": evento_envio,
                }
            )
        else:
            tiempo_txt, dato_evento = [p.strip() for p in linea.split(",", maxsplit=1)]
            nodo, evento = _parse_nodo_evento(dato_evento)
            tiempo = _parse_tiempo(tiempo_txt)

            eventos_por_nodo[nodo].append(
                {
                    "tipo": "local",
                    "t": tiempo,
                    "evento": evento,
                }
            )

            eventos_ordenados.append(
                {
                    "tipo": "local",
                    "t": tiempo,
                    "nodo": nodo,
                    "evento": evento,
                }
            )

    # Prioridad simple para empates: local/send antes de recv.
    prioridad_tipo = {"local": 0, "send": 1, "recv": 2}
    eventos_ordenados.sort(key=lambda e: (e["t"], prioridad_tipo[e["tipo"]], e["nodo"], e["evento"]))

    return {
        "nombre": ruta.name,
        "nodos": nodos,
        "eventos_por_nodo": eventos_por_nodo,
        "eventos_ordenados": eventos_ordenados,
    }


def cargar_caso_desde_archivo(ruta_test: str) -> dict:
    return parsear_test(ruta_test)
