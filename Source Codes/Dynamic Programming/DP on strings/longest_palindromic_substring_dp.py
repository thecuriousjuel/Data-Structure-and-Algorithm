def display(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print()
        
def fun(s1, s2, ind1, ind2, dp):
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    #print(ind1, ind2)
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]:
        dp[ind1][ind2] = 1 + fun(s1, s2, ind1-1, ind2-1, dp)
        return dp[ind1][ind2]

    left = fun(s1, s2, ind1, ind2-1, dp)
    right = fun(s1, s2, ind1-1, ind2, dp)
    
    dp[ind1][ind2] = max(left, right)
    
    return dp[ind1][ind2]


s1 = 'bbabcbcab'
s2 = s1[::-1]


ind1 = len(s1)
ind2 = len(s2)

dp = [[-1 for _ in range(ind2)] for _ in range(ind1)]
    
out = fun(s1, s2, ind1-1, ind2-1, dp)

print(out)
#display(dp)