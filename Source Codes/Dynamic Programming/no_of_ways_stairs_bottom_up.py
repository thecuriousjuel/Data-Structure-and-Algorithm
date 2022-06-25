def fun(n, mydict):

    if n <= 1:
        return 1

    if n in mydict.keys():
        return mydict[n]

    l = fun(n-1, mydict)
    r = fun(n-2, mydict)

    mydict[n-1] = l
    mydict[n-2] = r

    return l + r


mydict = {}
print(fun(5, mydict))