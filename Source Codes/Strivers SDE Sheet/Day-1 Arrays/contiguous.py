arr = [-2,1,-3,4,-1,2,1,-5,4]


for i in range(len(arr)):
    for j in range(i+1, len(arr) + 1):
        print(arr[i:j])
