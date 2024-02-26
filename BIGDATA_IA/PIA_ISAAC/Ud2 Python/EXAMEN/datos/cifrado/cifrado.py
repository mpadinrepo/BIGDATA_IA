

if __name__ == "__main__":
    rsa = Cifrador(3, 11)
    publica = rsa.clavePublica
    privada = rsa.clavePrivada

    cadena = [14, 2, 4]
    cifrado = publica.procesar(cadena)
    descifrado = privada.procesar(cifrado)
    print(f"Orixinal: {cadena}")
    print(f"Cifrado: {cifrado}")
    print(f"Descifrado: {descifrado}")
    assert cadena == descifrado
    