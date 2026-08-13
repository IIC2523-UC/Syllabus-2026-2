from sys import argv
from typing import Any
import requests


class ClienteNotasHTTP:
    def __init__(self, base_url: str = "http://127.0.0.1:5000") -> None:
        self.base_url = base_url

    def crear_evaluacion(self, evaluacion: str) -> Any:
        response = requests.post(
            f"{self.base_url}/evaluaciones",
            json={"evaluacion": evaluacion},
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    def registrar_nota(self, evaluacion: str, alumno: str, nota: float) -> Any:
        response = requests.post(
            f"{self.base_url}/notas",
            json={"evaluacion": evaluacion, "alumno": alumno, "nota": nota},
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    def obtener_nota(self, alumno: str, evaluacion: str) -> Any:
        response = requests.get(
            f"{self.base_url}/nota",
            params={"alumno": alumno, "evaluacion": evaluacion},
            timeout=5,
        )
        response.raise_for_status()
        return response.json()

    def listar_notas_alumno(self, alumno: str) -> Any:
        response = requests.get(f"{self.base_url}/notas/{alumno}", timeout=5)
        response.raise_for_status()
        return response.json()

    def promedio_evaluacion(self, evaluacion: str) -> Any:
        response = requests.get(f"{self.base_url}/promedio/{evaluacion}", timeout=5)
        response.raise_for_status()
        return response.json()

    def stats_avanzadas(self, evaluacion: str) -> Any:
        response = requests.get(f"{self.base_url}/stats/{evaluacion}", timeout=5)
        response.raise_for_status()
        return response.json()


def demo(port: int) -> None:
    cliente = ClienteNotasHTTP(base_url=f"http://127.0.0.1:{port}")

    print("Creando evaluaciones...")
    print("Retorno crear T1:", cliente.crear_evaluacion("T1"))
    print("Retorno crear T2:", cliente.crear_evaluacion("T2"))
    print("Retorno crear T3:", cliente.crear_evaluacion("T3"))
    print("Retorno crear T4:", cliente.crear_evaluacion("T4"))

    print("\nRegistrando notas...")
    # Ana: 4 notas
    print("Cantidad de notas de Ana:", cliente.registrar_nota("T1", "Ana", 6.1))
    print("Cantidad de notas de Ana:", cliente.registrar_nota("T2", "Ana", 5.4))
    print("Cantidad de notas de Ana:", cliente.registrar_nota("T3", "Ana", 6.7))
    print("Cantidad de notas de Ana:", cliente.registrar_nota("T4", "Ana", 5.9))

    # Ben: 3 notas
    print("Cantidad de notas de Ben:", cliente.registrar_nota("T1", "Ben", 4.7))
    print("Cantidad de notas de Ben:", cliente.registrar_nota("T2", "Ben", 5.1))
    print("Cantidad de notas de Ben:", cliente.registrar_nota("T3", "Ben", 5.8))

    # Carla: 2 notas
    print("Cantidad de notas de Carla:", cliente.registrar_nota("T1", "Carla", 6.5))
    print("Cantidad de notas de Carla:", cliente.registrar_nota("T4", "Carla", 6.0))

    # Diego: 1 nota
    print("Cantidad de notas de Diego:", cliente.registrar_nota("T2", "Diego", 4.9))

    print("\nConsultas...")
    print("Nota de Ana en T1:", cliente.obtener_nota("Ana", "T1"))
    print("Nota de Ben en T3:", cliente.obtener_nota("Ben", "T3"))
    print("Nota de Carla en T4:", cliente.obtener_nota("Carla", "T4"))
    print("Nota de Diego en T1 (no existe):", cliente.obtener_nota("Diego", "T1"))

    print("Notas de Ana:", cliente.listar_notas_alumno("Ana"))
    print("Notas de Ben:", cliente.listar_notas_alumno("Ben"))
    print("Notas de Carla:", cliente.listar_notas_alumno("Carla"))
    print("Notas de Diego:", cliente.listar_notas_alumno("Diego"))

    print("Promedio T1:", cliente.promedio_evaluacion("T1"))
    print("Promedio T2:", cliente.promedio_evaluacion("T2"))
    print("Promedio T3:", cliente.promedio_evaluacion("T3"))
    print("Promedio T4:", cliente.promedio_evaluacion("T4"))

    print("Stats T1:", cliente.stats_avanzadas("T1"))
    print("Stats T2:", cliente.stats_avanzadas("T2"))
    print("Stats T3:", cliente.stats_avanzadas("T3"))
    print("Stats T4:", cliente.stats_avanzadas("T4"))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Uso: python3 cliente.py <puerto>")
        exit(1)

    puerto = int(argv[1])

    try:
        demo(puerto)
    except requests.RequestException as error:
        print("Error HTTP:", error)
        print("Recuerda levantar primero el servidor Flask con 'python3 servidor.py <puerto>'.")
