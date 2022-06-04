def linearly(num, N):
    if num > N:
        return

    linearly(num+1, N)
    print(num)

linearly(num=1, N=5)