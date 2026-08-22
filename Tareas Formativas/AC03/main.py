from sys import argv

from parser_tests import cargar_caso_desde_archivo


def calcular_vector_logico(caso: dict) -> list[dict]:
    """
    TODO: implementar reloj vectorial.

    Entrada:
    - caso: diccionario generado por parser_tests.py

    Salida esperada:
    - lista de dicts con al menos: t, nodo, evento, tipo, vector
    """
    print(caso["nombre"])
    print(caso["nodos"])
    resultados = []
    for evento in caso["eventos_ordenados"]:
        print(evento)
        vector_evento = []
        # TODO: calcular el vector lógico del evento.



        resultados.append(
            {
                "t": evento["t"],
                "nodo": evento["nodo"],
                "evento": evento["evento"],
                "tipo": evento["tipo"],
                "vector": vector_evento,
            }
        )
    return resultados


def imprimir_resultados(nombre_caso: str, resultados: list[dict]) -> None:
    print(f"\n== {nombre_caso} ==")
    for resultado in resultados:
        t = resultado["t"]
        nodo = resultado["nodo"]
        evento = resultado["evento"]
        tipo = resultado["tipo"]
        vector = resultado["vector"]
        print(f"T{t}: {nodo}-{evento} ({tipo}) -> V={vector}")


def main() -> None:
    if len(argv) != 2:
        print("Uso: python3 main.py <ruta_test>")
        return

    ruta_test = argv[1]
    caso = cargar_caso_desde_archivo(ruta_test)
    resultados = calcular_vector_logico(caso)
    imprimir_resultados(caso["nombre"], resultados)


if __name__ == "__main__":
    main()
