def fun(str1, str2):
    
    len1 = len(str1)
    len2 = len(str2)
    
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    
    for i in range(len1+1):
        dp[i][0] = 1

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            
    return dp[len1][len2]
    


str1 = 'rabbbit'
str2 = 'rabbit'

out = fun(str1, str2)
print(out)

