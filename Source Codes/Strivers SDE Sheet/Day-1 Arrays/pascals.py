def fact(num):
    if num <= 1:
        return 1

    return fact(num - 1) * num

n = 5

for r in range(1, n+1):

    for _ in range(n-r+1):
        print(' ', end='')

    for c in range(1, r+1):
        print(fact(r-1)//(fact(c-1)*fact(r-c)), end = ' ')
    print()

