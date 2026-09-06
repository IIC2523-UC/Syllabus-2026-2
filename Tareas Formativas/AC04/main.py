from sys import argv

from parser_tests import cargar_caso_desde_archivo


def determinar_lider(caso: dict) -> dict:
    """
    TODO: implementar la eleccion de lider de Raft (una unica ronda de votación por el primer nodo candidato).

    Entrada:
    - caso: diccionario generado por parser_tests.py

    Salida esperada: un dict con al menos:
    - candidato: nodo que inicio la eleccion
    - term_nuevo: term del candidato finalizada la eleccion
    - votos: dict {nodo: True/False} indicando si cada nodo (salvo el candidato) le dio su voto
    - lider: True si el candidato consigue mayoria y gana esta ronda, False si no
    """
    resultado = {
        "candidato": None,
        "term_nuevo": None,
        "votos": {},
        "lider": False,
    }
    # TODO: implementar la eleccion segun las reglas de Raft vistas en clase.



    return resultado


def imprimir_info_nodos(caso: dict) -> None:
    print(f"\n== {caso['nombre']} ==")
    for nodo in caso["nodos"]:
        info = caso["info_nodos"][nodo]
        log = info["log"]
        ultimo_term_log = log[-1]["term"] if log else None
        print(f"  {nodo}: timeout={info['timeout']}, term={info['term']}, largo_log={len(log)}, ultimo_term_log={ultimo_term_log}")


def imprimir_resultado(resultado: dict) -> None:
    print("\n-- Resultado --")
    candidato = resultado["candidato"]
    print(f"Candidato: {candidato} (term nuevo: {resultado['term_nuevo']})")

    for nodo, voto in resultado["votos"].items():
        decision = "acepta" if voto else "rechaza"
        print(f"  {nodo} {decision} al candidato")

    if resultado["lider"]:
        print(f"{candidato} gana la eleccion y se convierte en lider.")
    else:
        print(f"{candidato} no consigue mayoria. Otro nodo deberá iniciar la elección para encontrar líder.")


def main() -> None:
    if len(argv) != 2:
        print("Uso: python3 main.py <ruta_test>")
        return

    ruta_test = argv[1]
    caso = cargar_caso_desde_archivo(ruta_test)
    imprimir_info_nodos(caso)
    resultado = determinar_lider(caso)
    imprimir_resultado(resultado)


if __name__ == "__main__":
    main()
