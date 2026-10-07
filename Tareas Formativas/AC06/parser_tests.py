from pathlib import Path


def _parsear_evento(t: int, linea: str) -> dict:
    partes = [parte.strip() for parte in linea.split(";")]
    replica, cliente, tipo, variable = partes[0], partes[1], partes[2].upper(), partes[3]

    evento = {
        "t": t,
        "replica": replica,
        "cliente": cliente,
        "tipo": tipo,
        "variable": variable,
    }
    if tipo == "W":
        evento["version_anterior"] = int(partes[4])
        evento["version"] = int(partes[5])
    else:
        evento["version"] = int(partes[4])

    return evento


def parsear_test(ruta_test: str) -> dict:
    ruta = Path(ruta_test)
    lineas = [
        linea.strip()
        for linea in ruta.read_text(encoding="utf-8").splitlines()
        if linea.strip()
    ]

    if not lineas:
        raise ValueError(f"Archivo vacio: {ruta_test}")

    replicas = [replica.strip() for replica in lineas[0].split(",") if replica.strip()]
    clientes = [cliente.strip() for cliente in lineas[1].split(",") if cliente.strip()]
    eventos_ordenados = [
        _parsear_evento(t, linea) for t, linea in enumerate(lineas[2:], start=1)
    ]

    return {
        "nombre": ruta.name,
        "replicas": replicas,
        "clientes": clientes,
        "eventos_ordenados": eventos_ordenados,
    }


def cargar_caso_desde_archivo(ruta_test: str) -> dict:
    return parsear_test(ruta_test)
