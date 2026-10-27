import hashlib
import secrets


def _mcd(a, b):
    while b:
        a, b = b, a % b
    return a


def _inverso_modular(a, m):
    def euclides_extendido(a, b):
        if b == 0:
            return a, 1, 0

        mcd, x, y = euclides_extendido(b, a % b)

        return mcd, y, x - (a // b) * y

    mcd, x, _ = euclides_extendido(a, m)

    if mcd != 1:
        raise ValueError("No existe inverso modular.")

    return x % m


def _es_primo(n, rondas=20):

    if n < 2:
        return False

    primos_pequenos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for p in primos_pequenos:
        if n == p:
            return True

        if n % p == 0:
            return False

    d = n - 1
    s = 0

    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(rondas):
        a = secrets.randbelow(n - 3) + 2

        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            return False

    return True


def _generar_primo(bits):

    while True:
        numero = secrets.randbits(bits)

        numero |= 1 << (bits - 1)
        numero |= 1

        if _es_primo(numero):
            return numero


# ============================================================
# GENERACIÓN DE CLAVES
# ============================================================


def generar_claves(bits=512):

    while True:
        p = _generar_primo(bits // 2)
        q = _generar_primo(bits // 2)

        if p == q:
            continue

        n = p * q

        phi = (p - 1) * (q - 1)

        e = 65537

        if _mcd(e, phi) != 1:
            continue

        d = _inverso_modular(e, phi)

        clave_publica = (e, n)
        clave_privada = (d, n)

        return clave_publica, clave_privada


# ============================================================
# CIFRADO
# ============================================================


def cifrar(mensaje, clave_publica):

    e, n = clave_publica

    tamano_bloque = (n.bit_length() - 1) // 8

    resultado = []

    for inicio in range(0, len(mensaje), tamano_bloque):
        bloque = mensaje[inicio : inicio + tamano_bloque]

        numero = int.from_bytes(bloque, byteorder="big")

        cifrado = pow(numero, e, n)

        resultado.append(cifrado.to_bytes((n.bit_length() + 7) // 8, byteorder="big"))

    return b"".join(resultado)


# ============================================================
# DESCIFRADO
# ============================================================


def descifrar(datos, clave_privada):

    d, n = clave_privada

    tamano_cifrado = (n.bit_length() + 7) // 8

    resultado = bytearray()

    for inicio in range(0, len(datos), tamano_cifrado):
        bloque = datos[inicio : inicio + tamano_cifrado]

        numero = int.from_bytes(bloque, byteorder="big")

        descifrado = pow(numero, d, n)

        tamano_original = (descifrado.bit_length() + 7) // 8

        if tamano_original > 0:
            resultado.extend(descifrado.to_bytes(tamano_original, byteorder="big"))

    return bytes(resultado)


# ============================================================
# FIRMA
# ============================================================


def firmar(mensaje, clave_privada):

    d, n = clave_privada

    hash_mensaje = hashlib.sha256(mensaje).digest()

    numero = int.from_bytes(hash_mensaje, byteorder="big")

    firma = pow(numero, d, n)

    return firma.to_bytes((n.bit_length() + 7) // 8, byteorder="big")


# ============================================================
# VERIFICACIÓN
# ============================================================


def verificar(mensaje, firma, clave_publica):

    e, n = clave_publica

    hash_mensaje = hashlib.sha256(mensaje).digest()

    numero_firma = int.from_bytes(firma, byteorder="big")

    numero_hash = pow(numero_firma, e, n)

    hash_recuperado = numero_hash.to_bytes((n.bit_length() + 7) // 8, byteorder="big")

    hash_recuperado = hash_recuperado[-len(hash_mensaje) :]

    return hash_recuperado == hash_mensaje


# ============================================================
# PRUEBA
# ============================================================

if __name__ == "__main__":
    print("Generando claves...")

    publica, privada = generar_claves(512)

    print("Clave pública:")
    print(publica)

    print("\nClave privada:")
    print(privada)

    mensaje = b"Hola, este es un mensaje de prueba."

    print("\nMensaje original:")
    print(mensaje)

    cifrado = cifrar(mensaje, publica)

    print("\nMensaje cifrado:")
    print(cifrado)

    recuperado = descifrar(cifrado, privada)

    print("\nMensaje recuperado:")
    print(recuperado)

    print("\nMensaje correcto:")
    print(recuperado == mensaje)

    firma = firmar(mensaje, privada)

    print("\nFirma:")
    print(firma)

    print("\nFirma valida:")
    print(verificar(mensaje, firma, publica))
