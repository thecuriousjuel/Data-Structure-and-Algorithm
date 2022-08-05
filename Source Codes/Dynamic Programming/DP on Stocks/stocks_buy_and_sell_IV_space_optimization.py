def fun(arr, kk):
    
    cur = [[0 for _ in range(kk+1)] for _ in range(2)]
    next = [[0 for _ in range(kk+1)] for _ in range(2)]
    
    for ind in range(len(arr)-1, -1, -1):
        for buy in range(2):
            for k in range(1, kk+1):
    
                if buy == 1:
                    profit = max(-arr[ind] + next[0][k], 0 + next[1][k])
                    
                else:
                    profit = max(arr[ind] + next[1][k-1], 0 + next[0][k])
                    
                cur[buy][k] = profit
                
        next = cur
        
    print(cur)
    print(next)
                
    return next[1][kk]



arr = [48,12,60,93,97,42,25,64,17,56,85,93,9,48,52,42,58,85,81,84,69,36,1,54,23,15,72,15,11,94]
kk=7

out = fun(arr, kk)
print(out)


