from pathlib import Path


def _parsear_operacion(linea: str) -> dict:
    partes = [parte.strip() for parte in linea.split(";")]
    transaccion = partes[0]
    accion = partes[1].upper()

    operacion = {"transaccion": transaccion, "accion": accion}
    if accion in {"READ", "WRITE"}:
        operacion["variable"] = partes[2]
    return operacion


def parsear_test(ruta_test: str) -> dict:
    ruta = Path(ruta_test)
    lineas = [
        linea.strip()
        for linea in ruta.read_text(encoding="utf-8").splitlines()
        if linea.strip()
    ]

    if not lineas:
        raise ValueError(f"Archivo vacio: {ruta_test}")

    transacciones = [
        transaccion.strip()
        for transaccion in lineas[0].split(",")
        if transaccion.strip()
    ]
    operaciones = [_parsear_operacion(linea) for linea in lineas[1:]]

    return {
        "nombre": ruta.name,
        "transacciones": transacciones,
        "operaciones": operaciones,
    }


def cargar_caso_desde_archivo(ruta_test: str) -> dict:
    return parsear_test(ruta_test)