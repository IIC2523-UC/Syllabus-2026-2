from sys import argv
from parser_tests import cargar_caso_desde_archivo


def validar_commit(transaccion_a_commitear: dict, transacciones_activas: dict) -> bool:
    """TODO: devolver True si la transaccion puede hacer COMMIT."""
    return False


def evaluar_caso(caso: dict) -> dict:
    """TODO: devolver {transaccion: "COMMIT" o "ABORT"}."""
    transacciones = {
        transaccion: {
            "id": transaccion,
            "reads": set(),
            "writes": set(),
        }
        for transaccion in caso["transacciones"]
    }
    # Resultados iniciales: todas las transacciones abortan
    resultados = {transaccion: "ABORT" for transaccion in caso["transacciones"]}

    transacciones_activas = {}

    for operacion in caso["operaciones"]:
        transaccion_id = operacion["transaccion"]
        transaccion = transacciones[transaccion_id]
        accion = operacion["accion"]

        print(f"Procesando {accion} de {transaccion_id}")
        # Actualizar "resultados" según corresponda.


    return resultados


def imprimir_resultado(caso: dict, resultado: dict) -> None:
    print(f"\n== {caso['nombre']} ==")
    print(resultado)


def main() -> None:
    if len(argv) != 2:
        print("Uso: python3 main.py <ruta_test>")
        return

    caso = cargar_caso_desde_archivo(argv[1])
    resultado = evaluar_caso(caso)
    imprimir_resultado(caso, resultado)


if __name__ == "__main__":
    main()