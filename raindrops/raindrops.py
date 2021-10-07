def convert(numero):
    sonido = ""
    if numero % 3 == 0:
        sonido += "Pling"
    if numero % 5 == 0:
        sonido += "Plang"
    if numero % 7 == 0:
        sonido += "Plong"
    return sonido if sonido != "" else str(numero)