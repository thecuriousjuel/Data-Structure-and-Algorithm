# TC -> O(n^3)


arr = [-2,1,-3,4,-1,2,1,-5,4]
max_sum = float('-inf')
max_array = []

for i in range(len(arr)):
    for j in range(i+1, len(arr) + 1):
        if sum(arr[i:j]) > max_sum:
            max_sum = sum(arr[i:j])
            max_array = arr[i:j]
        

print(max_array, max_sum)