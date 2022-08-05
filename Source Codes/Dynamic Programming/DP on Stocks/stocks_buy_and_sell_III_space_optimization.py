def fun(arr):
    
    i = len(arr)
    j = 2
    k = 2
    
    prev = [[0 for _ in range(k+1)] for _ in range(j)]
    cur = [[0 for _ in range(k+1)] for _ in range(j)]
    
    for ind in range(i-1, -1, -1):
        for buy in range(j):
            for count in range(1, k+1):

                if buy:
                    profit = max(-arr[ind] + prev[0][count],
                                 0 + prev[1][count])
                else:
                    profit = max(arr[ind] + prev[1][count-1],
                                 0 + prev[0][count])
                    
                cur[buy][count] = profit
                
        prev = cur
                
    return cur[1][2]



arr = [3,3,5,0,0,3,1,4]
out = fun(arr)
print(out)


