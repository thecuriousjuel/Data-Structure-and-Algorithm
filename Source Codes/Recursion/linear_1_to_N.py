from pyparsing import line


def linear(num, n):
    if num > n:
        return

    print(num)
    linear(num+1, n)

linear(1, 5)