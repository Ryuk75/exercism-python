def slices(series, length):
    longt = len(series)
    if length > longt or length <= 0:
        raise ValueError('La longitud tiene que ser mayor a cero y menor que {longt+1} con la serie.')
    return [series[x:x + length] for x in range((longt - length)+1)]