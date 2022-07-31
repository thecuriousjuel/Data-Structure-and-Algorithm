def fun(str1, str2):
    
    n = len(str1)
    m = len(str2)
    
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    
    dp[0][0] = True
    
    for j in range(1, m+1):
        dp[0][j] = False
        
    for i in range(1, n+1):
        flag = True
        for ii in range(0, i):
            if str1[ii] != '*':
                flag = False
                break
    
    
    dp[i][0] = flag
    
    for ind1 in range(1, n+1):
        for ind2 in range(1, m+1):

            if str1[ind1-1] == str2[ind2-1] or str1[ind1-1] == '?':
                dp[ind1][ind2] = dp[ind1-1][ind2-1]
                
            elif str1[ind1-1] == '*':
                left = dp[ind1-1][ind2]
                right = dp[ind1][ind2-1]
                dp[ind1][ind2] = left or right
            
            else:
                dp[ind1][ind2] = False
                
    return dp[n][m]


str1 = 'ab?cd'
str2 = 'abgcd'

out = fun(str1, str2)
print(out)



