from pathlib import Path


def _parsear_log(texto: str) -> list[dict]:
    texto = texto.strip()
    if not texto:
        return []

    log = []
    for entrada in texto.split(","):
        accion, term_txt = entrada.strip().split("-")
        log.append({"accion": accion.strip(), "term": int(term_txt)})
    return log


def parsear_test(ruta_test: str) -> dict:
    ruta = Path(ruta_test)
    lineas = [linea.strip() for linea in ruta.read_text(encoding="utf-8").splitlines() if linea.strip()]

    if not lineas:
        raise ValueError(f"Archivo vacio: {ruta_test}")

    nodos = [nodo.strip() for nodo in lineas[0].split(",") if nodo.strip()]
    info_nodos = {}

    for linea in lineas[1:]:
        nodo, term_txt, timeout_txt, log_txt = linea.split(";", maxsplit=3)

        info_nodos[nodo.strip()] = {
            "term": int(term_txt.strip()),
            "timeout": int(timeout_txt.strip()),
            "log": _parsear_log(log_txt),
        }

    return {
        "nombre": ruta.name,
        "nodos": nodos,
        "info_nodos": info_nodos,
    }


def cargar_caso_desde_archivo(ruta_test: str) -> dict:
    return parsear_test(ruta_test)
