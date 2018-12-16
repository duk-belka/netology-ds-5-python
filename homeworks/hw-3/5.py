def sum_fibonacci(n=5):
    f0, f1 = [0, 1]
    n_sum = 1
    n -= 2
    while n > 0:
        n -= 1
        f2 = f1 + f0
        f0, f1 = f1, f2
        n_sum += f2
    return n_sum


print(sum_fibonacci())
