def fun(arr):
    
    n = len(arr)
    dp = [0 for _ in range(n+1)]
    
    dp[n] = True
    
    for ind in range(n-1, -1, -1):
        k = arr[ind]
        temp = False
        
        for i in range(1, k+1):
            if ind + i < len(arr):
                temp = temp or dp[ind+i]
            
        dp[ind] = temp
        
    print(dp)
    return dp[ind]
    
  
arr = [2,3,1,1,4]

out = fun(arr)

print(out)
