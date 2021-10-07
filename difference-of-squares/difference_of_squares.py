def square_of_sum(numero):
    return sum([num for num in range(numero + 1)])**2


def sum_of_squares(numero):
    return sum([num**2 for num in range(numero + 1)])


def difference_of_squares(numero):
    return abs(square_of_sum(numero) - sum_of_squares(numero))