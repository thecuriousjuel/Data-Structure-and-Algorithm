def linearly(num):
    if num < 1:
        return

    linearly(num-1)
    print(num)


linearly(5)
