def fun(arr):
    
    n = len(arr)
    dp = [0 for _ in range(n)]
    
    dp[n-1] = True
    
    for ind in range(n-2, -1, -1):
        k = arr[ind]
        temp = False
        
        for i in range(1, k+1):
            if ind + i < len(arr):
                temp = temp or dp[ind+i]
            
        dp[ind] = temp
        
    return dp[0]
    
  
arr = [i for i in range(1000)]

out = fun(arr)

print(out)
