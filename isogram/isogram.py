def is_isogram(frase):
    buscar = set([]) 
    for x in frase.lower():
        if (x.isalpha()):
            if (x in buscar):
                return False
            else:
                buscar.add(x)
    return True