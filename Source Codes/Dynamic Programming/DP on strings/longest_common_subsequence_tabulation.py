def fun(str1, str2):
    
    ind1 = len(str1)
    ind2 = len(str2)

    dp = [[-1 for _ in range(ind2+1)] for _ in range(ind1+1)]
    
    for i in range(ind1+1):
        dp[i][0] = 0
    
    for j in range(ind2+1):
        dp[0][j] = 0
    
    for i in range(1, ind1+1):
        
        for j in range(1, ind2+1):
    
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
    
            else:
                left = dp[i-1][j]
                right = dp[i][j-1]
    
                dp[i][j] = max(left, right)

    #print(dp)
    return dp[i][j]
    

str1 = 'fede'
str2 = 'fede'

out = fun(str1, str2)
print(out)



