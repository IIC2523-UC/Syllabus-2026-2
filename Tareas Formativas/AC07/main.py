import hashlib
import rsa
import time


# Funciones auxiliares para simular
# cifrado y descifrado simétrico, y aplicación de hash.
def cifrar_simetrico(mensaje, clave):
    return bytes(byte ^ clave for byte in mensaje)


def descifrar_simetrico(mensaje, clave):
    return bytes(byte ^ clave for byte in mensaje)


def cifrar_asimetrico(mensaje, clave_publica):
    return rsa.cifrar(mensaje, clave_publica)


def descifrar_asimetrico(mensaje, clave_privada):
    return rsa.descifrar(mensaje, clave_privada)


def calcular_hash(mensaje):
    return hashlib.sha256(mensaje).digest()


def firmar_hash(hash_mensaje, clave_privada):
    return rsa.firmar(hash_mensaje, clave_privada)


def verificar_hash(hash_mensaje, firma, clave_publica):
    return rsa.verificar(hash_mensaje, firma, clave_publica)

####################################
# Pipelines (Esto debes completar)
####################################
def pipeline_simetrico(mensaje, clave_simetrica):
    """
    Completa el pipeline de cifrado y descifrado simétrico.
    Debes retornar el mensaje recuperado después de cifrar y descifrar.
    """
    # Etapa Emisor
    
    
    # Etapa Receptor

    return ""


def pipeline_asimetrico(mensaje, clave_publica, clave_privada):
    """
    Completa el pipeline de cifrado y descifrado asimétrico.
    Debes retornar el mensaje recuperado después de cifrar y descifrar.
    """
    # Etapa Emisor


    # Etapa Receptor

    return ""


def pipeline_hash(mensaje, clave_publica, clave_privada):
    """
    Completa el pipeline de hash y firma digital.
    Debes retornar True si la verificación es correcta, o False en caso contrario.
    """
    # Etapa Emisor


    # Etapa Receptor

    return False


# Medición
def medir_tiempos(clave_simetrica, clave_publica, clave_privada):
    tamanos = [100, 1000, 10000, 100000, 1000000]
    resultados = {"simetrico": [], "asimetrico": [], "hash_rsa": []}

    for tamano in tamanos:
        print()
        print("=" * 60)
        print(f"Mensaje de {tamano:,} bytes")
        print("=" * 60)

        mensaje = b"A" * tamano

        inicio = time.perf_counter()
        mensaje_recuperado = pipeline_simetrico(mensaje, clave_simetrica)
        fin = time.perf_counter()
        tiempo = fin - inicio
        assert mensaje_recuperado == mensaje
        resultados["simetrico"].append(tiempo)
        print(f"Simétrico:          {tiempo:.6f} segundos")

        inicio = time.perf_counter()
        mensaje_recuperado = pipeline_asimetrico(
            mensaje,
            clave_publica,
            clave_privada
        )
        fin = time.perf_counter()
        tiempo = fin - inicio
        assert mensaje_recuperado == mensaje
        resultados["asimetrico"].append(tiempo)
        print(f"Asimétrico:         {tiempo:.6f} segundos")

        inicio = time.perf_counter()
        resultado = pipeline_hash(
            mensaje,
            clave_publica,
            clave_privada
        )
        fin = time.perf_counter()
        tiempo = fin - inicio
        assert resultado is True
        resultados["hash_rsa"].append(tiempo)
        print(f"Hash + Asimétrico:  {tiempo:.6f} segundos")

    return tamanos, resultados


def main():
    clave_simetrica = 123
    print("Generando claves RSA...")
    clave_publica, clave_privada = rsa.generar_claves(512)
    print("Claves generadas.")

    medir_tiempos(clave_simetrica, clave_publica, clave_privada)


# Ejecución
if __name__ == "__main__":
    main()
