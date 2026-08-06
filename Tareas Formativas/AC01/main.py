import random
import threading
import time


data = [0]
CANTIDAD_THREADS = 20
INCREMENTOS_POR_THREAD = 10
CANTIDAD_CORRIDAS = 5

# Estructuras compartidas del algoritmo del panadero.
eligiendo = [False] * CANTIDAD_THREADS
numero = [0] * CANTIDAD_THREADS


def reiniciar_panadero() -> None:
    for i in range(CANTIDAD_THREADS):
        eligiendo[i] = False
        numero[i] = 0


def algoritmo_panadero_lamport(thread_id: int) -> None:
    for _ in range(INCREMENTOS_POR_THREAD):
        # COMPLETAR con panadero de Lamport



        # Empezar Seccion critica
        increment()
        # Terminar seccion critica


def increment() -> None:
    # Separa lectura y escritura para que la condicion de carrera sea visible.
    valor = data[0] + 1
    time.sleep(random.uniform(0.0, 0.001))
    data[0] = valor
    time.sleep(random.uniform(0.0, 0.001))


def worker_sin_sincronizacion() -> None:
    for _ in range(INCREMENTOS_POR_THREAD):
        increment()


def correr_sin_sincronizacion() -> None:
    esperado = CANTIDAD_THREADS * INCREMENTOS_POR_THREAD
    print("Sin sincronizacion:")

    for corrida in range(1, CANTIDAD_CORRIDAS + 1):
        data[0] = 0
        threads = []
        for _ in range(CANTIDAD_THREADS):
            thread = threading.Thread(target=worker_sin_sincronizacion)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Corrida {corrida}: esperado={esperado}, obtenido={data[0]}")


def correr_con_panadero() -> None:
    esperado = CANTIDAD_THREADS * INCREMENTOS_POR_THREAD
    print("\nCon algoritmo del panadero de Lamport:")

    for corrida in range(1, CANTIDAD_CORRIDAS + 1):
        data[0] = 0
        reiniciar_panadero()
        threads = []
        for thread_id in range(CANTIDAD_THREADS):
            thread = threading.Thread(
                target=algoritmo_panadero_lamport,
                args=(thread_id,),
            )
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        print(f"Corrida {corrida}: esperado={esperado}, obtenido={data[0]}")


if __name__ == "__main__":
    correr_sin_sincronizacion()

    # Pendiente: actualizar esta función para que implemente el algoritmo del panadero de Lamport.
    correr_con_panadero()