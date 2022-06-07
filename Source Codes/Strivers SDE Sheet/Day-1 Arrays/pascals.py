arr = []
arr.append([1])
n = 5


for i in range(n-1):
    arr.append([1, 1])


for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j + 2 <= len(arr[i]):
            if i + 1 <= len(arr[i]):
                print(sum(arr[i][j::2]))
                arr[i+1].insert(j+2-1, sum(arr[i][j::2]))


print(arr)
