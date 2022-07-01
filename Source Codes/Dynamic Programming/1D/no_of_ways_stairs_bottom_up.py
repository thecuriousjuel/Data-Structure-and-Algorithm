def fun(n, mydict):

    if n <= 1:
        return 1

    if n in mydict.keys():
        return mydict[n]

    mydict[n] = fun(n-1, mydict) + fun(n-2, mydict)

    return mydict[n]


mydict = {}
print(fun(6, mydict))