def fun(s1, s2, ind1, ind2):
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        return 1 + fun(s1, s2, ind1-1, ind2-1)

    left = fun(s1, s2, ind1, ind2-1)
    right = fun(s1, s2, ind1-1, ind2)
    
    return max(left, right)


s1 = 'bbabcbcab'
s2 = s1[::-1]


ind1 = len(s1) - 1
ind2 = len(s2) - 1 
out = fun(s1, s2, ind1, ind2)

print(out)