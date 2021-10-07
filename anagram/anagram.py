def find_anagrams(palabra, candidatos):
    candidatoF = []
    palabra = palabra.lower()
    for palabras in candidatos:
        x = palabras.lower()
        if palabra != x and sorted(palabra) == sorted(x):
            candidatoF.append(palabras)
    return candidatoF