def nextLargerElement(arr, n):
    print(arr, n)

    # Base Case
    if len(arr) == 0:
        return [-1]

    if arr[0] > n:
        return [arr[0]] + nextLargerElement(arr[1:], arr[0])

    # Recursive Case

    value = nextLargerElement(arr[1:], arr[0])
    print(value)
    return value


print(nextLargerElement([1, 3, 2, 4, 1],  4))