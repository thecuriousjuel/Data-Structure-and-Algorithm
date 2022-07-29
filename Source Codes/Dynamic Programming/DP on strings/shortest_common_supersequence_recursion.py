def fun(str1, str2, ind1, ind2):
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if str1[ind1] == str2[ind2]:
        return 1 + fun(str1, str2, ind1-1, ind2-1)

    left = fun(str1, str2, ind1, ind2-1)
    right = fun(str1, str2, ind1-1, ind2)
    
    return max(left, right)
    
    
str1 = 'brute'
str2 = 'groot'

ind1 = len(str1)
ind2 = len(str2)

out = fun(str1, str2, ind1-1, ind2-1)
print(ind1+ ind2 - out)


