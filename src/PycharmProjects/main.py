def nextLargerElement(arr, n, stack=[], cmp=None):
    print(arr, cmp)
   #
    if n == 0:
        return -1

    if cmp:
        if arr[0] > cmp:
            return arr[0]
        else:
            return nextLargerElement(arr[1:], len(arr[1:]), cmp)

    return nextLargerElement(arr, len(arr), arr[1:], arr[0])


print(nextLargerElement([5, 3, 2, 4],  4))

