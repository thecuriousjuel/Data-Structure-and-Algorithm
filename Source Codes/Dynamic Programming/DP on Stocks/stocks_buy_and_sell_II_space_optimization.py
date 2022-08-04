def fun(arr):
    
    n = len(arr)
    
    prev = [0 for _ in range(2)]
    curr = [0 for _ in range(2)]

    for ind in range(n-1, -1, -1):
        for buy in range(2):

            if buy == True:
                profit = max(-arr[ind] + prev[0], 
                             0 + prev[1])

            else:
                profit = max(arr[ind] + prev[1], 
                             0 + prev[0])

            curr[buy] = profit
            
        curr, prev = prev, curr

    return prev[buy]

arr = [7,1,5,3,6,4]
out = fun(arr)
print(out)
