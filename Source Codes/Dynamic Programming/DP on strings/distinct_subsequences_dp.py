def fun(str1, str2, ind1, ind2, dp):
    if ind2 < 0:
        return 1
    
    if ind1 < 0:
        return 0
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    if str1[ind1] == str2[ind2]:
        return fun(str1, str2, ind1-1, ind2-1, dp) + fun(str1, str2, ind1-1, ind2, dp)
    
    dp[ind1][ind2] = fun(str1, str2, ind1-1, ind2, dp)
    
    return dp[ind1][ind2]
    


str1 = 'rabbbit'
str2 = 'rabbit'

ind1 = len(str1)
ind2 = len(str2)

dp = [[-1 for _ in range(ind2)] for _ in range(ind1)]

out = fun(str1, str2, ind1-1, ind2-1, dp)
print(out)

