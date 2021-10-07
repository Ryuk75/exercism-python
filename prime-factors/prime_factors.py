def factors(value):
    factorP = [] 
    n = 2
    while value > 1:
        while (value % n) == 0:
            factorP.append(n)
            value /= n
        n += 1
    return factorP