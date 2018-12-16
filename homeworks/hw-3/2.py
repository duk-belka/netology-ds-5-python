data = [1, '5', 'abc', 20, '2']


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def sum_sqr_of_num(data):
    sum = 0
    for item in data:
        if is_number(item):
            sum += float(item) ** 2
    return sum


print(sum_sqr_of_num(data))
