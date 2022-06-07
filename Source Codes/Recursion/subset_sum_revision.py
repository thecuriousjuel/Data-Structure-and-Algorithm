def subset(arr, index, l=[], sum_l = []):
    if index >= len(arr):
        sum_l.append(sum(l))
        return

    l.append(arr[index])
    subset(arr, index+1, l[:], sum_l)
    l.pop()

    subset(arr, index+1, l[:], sum_l)

    if index == 0:
        return sum_l


output = subset([5,2,1], 0)
print(sorted(output))