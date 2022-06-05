def sum_num(n):
    if n < 1:
        return 0

    return sum_num(n-1) + n


print(sum_num(5))