from sys import argv

from parser_tests import cargar_caso_desde_archivo


def verificar_monotonic_reads(caso: dict) -> dict:
    """TODO: implementar Monotonic Reads. Retorna dict {cliente: True/False}."""
    resultados = {cliente: True for cliente in caso["clientes"]}
    # TODO: recorrer caso["eventos_ordenados"] y actualizar resultados.



    return resultados


def verificar_read_your_writes(caso: dict) -> dict:
    """TODO: implementar Read Your Writes. Retorna dict {cliente: True/False}."""
    resultados = {cliente: True for cliente in caso["clientes"]}
    # TODO: recorrer caso["eventos_ordenados"] y actualizar resultados.



    return resultados


def verificar_monotonic_writes(caso: dict) -> dict:
    """Desafio bonus (opcional): implementar Monotonic Writes."""
    return {cliente: "No implementado, queda como bonus" for cliente in caso["clientes"]}


def verificar_writes_follow_reads(caso: dict) -> dict:
    """Desafio bonus (opcional): implementar Writes Follow Reads."""
    return {cliente: "No implementado, queda como bonus" for cliente in caso["clientes"]}


def imprimir_resultados(nombre_caso: str, propiedad: str, resultados: dict) -> None:
    print(f"\n== {nombre_caso} - {propiedad} ==")
    for cliente, resultado in resultados.items():
        print(f"  {cliente}: {resultado}")


def main() -> None:
    if len(argv) != 2:
        print("Uso: python3 main.py <ruta_test>")
        return

    ruta_test = argv[1]
    caso = cargar_caso_desde_archivo(ruta_test)

    imprimir_resultados(caso["nombre"], "Monotonic Reads", verificar_monotonic_reads(caso))
    imprimir_resultados(caso["nombre"], "Read Your Writes", verificar_read_your_writes(caso))
    imprimir_resultados(caso["nombre"], "Monotonic Writes (bonus)", verificar_monotonic_writes(caso))
    imprimir_resultados(caso["nombre"], "Writes Follow Reads (bonus)", verificar_writes_follow_reads(caso))


if __name__ == "__main__":
    main()
