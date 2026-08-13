from sys import argv
# Agregar imports necesarios para levantar el RPC



if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Uso: python3 servidor.py <puerto>")
        exit(1)

    IP = "127.0.0.1"
    PUERTO = int(argv[1])

    # Completar para levantar el RPC en el puerto indicado en PUERTO