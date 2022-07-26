def fun(str1, str2, ind1, ind2, dp):
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if str1[ind1] == str2[ind2]:
        dp[ind1][ind2] = 1 + fun(str1, str2, ind1-1, ind2-1, dp)
        return dp[ind1][ind2]
    
    left = fun(str1, str2, ind1-1, ind2, dp)
    right = fun(str1, str2, ind1, ind2-1, dp)
    
    dp[ind1][ind2] = max(left, right)

    return dp[ind1][ind2]
    

str1 = 'fede'
str2 = 'fede'

ind1 = len(str1)
ind2 = len(str2)

dp = [[-1 for _ in range(ind2)] for _ in range(ind1)]

out = fun(str1, str2, ind1-1, ind2-1, dp)
print(out)



