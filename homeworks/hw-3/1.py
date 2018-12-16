data = [
    [13, 25, 23, 34],
    [45, 32, 44, 47],
    [12, 33, 23, 95],
    [13, 53, 34, 35],
]


def diagonal_sum(data):
    """
    :param data: array of array of int
    :return: int
    """
    sum = 0
    i = 0
    for line in data:
        sum += line[i]
        i += 1
    return sum


print(diagonal_sum(data))
