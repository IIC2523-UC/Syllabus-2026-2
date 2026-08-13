from sys import argv
# Agregar imports necesarios para conectarte al RPC


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Uso: python3 cliente.py <puerto>")
        exit(1)

    IP = "127.0.0.1"
    PUERTO = int(argv[1])

    # Completar para crear el proxy RPC apuntando a IP y PUERTO
    # Completar para ejecutar un demo de llamadas remotas
