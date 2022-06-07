def subsequence(arr, index, sub_sum, output = [], t=[]):
    if index >= len(arr):
        if sum(t) == sub_sum:
            output.append(t)

        return

    t.append(arr[index])
    subsequence(arr, index+1, sub_sum, output, t[:])
    t.pop()
    subsequence(arr, index+1, sub_sum, output, t[:])

    if index == 0:
        return output

arr = [5,1,3,2]
sub_sum = 6
index = 0

print(subsequence(arr, index, sub_sum))