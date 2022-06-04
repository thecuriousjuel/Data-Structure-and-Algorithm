def linear(num):
    if num < 1:
        return

    print(num)
    linear(num - 1)

linear(5)