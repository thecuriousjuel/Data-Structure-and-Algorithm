def fun(n):

    if n <= 1:
        return 1

    l = fun(n-1)
    r = fun(n-2)

    return l + r



print(fun(30))