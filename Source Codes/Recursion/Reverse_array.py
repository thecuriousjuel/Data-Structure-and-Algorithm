def reverse_array(arr, n=None):

    if len(arr) <= 0:
        return []

    t = reverse_array(arr[1:], arr[0])
    t.append(arr[0])
    return t


arr = [3,4,5,6,1,9]
print(reverse_array(arr))