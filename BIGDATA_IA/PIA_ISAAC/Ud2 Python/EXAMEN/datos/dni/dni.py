
asociacion = [
    (0, 'T'),
    (1, 'R'),
    (2, 'W'),
    (3, 'A'),
    (4, 'G'),
    (5, 'M'),
    (6, 'Y'),
    (7, 'F'),
    (8, 'P'),
    (9, 'D'),
    (10, 'X'),
    (11, 'B'),
    (12, 'N'),
    (13, 'J'),
    (14, 'Z'),
    (15, 'S'),
    (16, 'Q'),
    (17, 'V'),
    (18, 'H'),
    (19, 'L'),
    (20, 'C'),
    (21, 'K'),
    (22, 'E')
]

if __name__ == "__main__":
    pass




    numeroLetra = {numero:letra for numero,letra in asociacion}
    def comprobar(dni:str)-> bool:
        numero=dni[0:8]
        letra=dni[8]
        n=int(numero)
        resto = n % 23
        letraCalculada = numeroLetra[resto]
        if letraCalculada

        
    #numeroLetra={}
    #   for numero,letra in asociacion:
    #   numeroLetra[] = letra

    print("Introduce DNI")
    dni= input()
    numero = dni [0:8]
    print (numero)
