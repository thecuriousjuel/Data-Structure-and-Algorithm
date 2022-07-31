def fun(str1, str2, ind1, ind2, dp):
    
    if ind1 == 0 and ind2 == 0:
        return True
    
    if ind1 == 0 and ind2 > 0:
        return False

    if ind2 == 0 and ind1 > 0:
        for i in range(0, ind1):
            if str1[i] != '*':
                return False
        return True
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]

    if str1[ind1-1] == str2[ind2-1] or str1[ind1-1] == '?':
        dp[ind1][ind2] = fun(str1, str2, ind1-1, ind2-1, dp)
        return dp[ind1][ind2]

    if str1[ind1-1] == '*':
        left = fun(str1, str2, ind1-1, ind2, dp)
        right = fun(str1, str2, ind1, ind2-1, dp)
        
        dp[ind1][ind2] = left or right
        return dp[ind1][ind2]

    dp[ind1][ind2] = False
    return dp[ind1][ind2]


str1 = 'ab*cd'
str2 = 'abefgcd'

ind1 = len(str1)
ind2 = len(str2)

dp = [[-1 for _ in range(ind2+1)] for _ in range(ind1+1)]

out = fun(str1, str2, ind1, ind2, dp)
print(out)



