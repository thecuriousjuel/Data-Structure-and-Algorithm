def fun(str1, str2, ind1, ind2):
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if str1[ind1] == str2[ind2]:
        return 1 + fun(str1, str2, ind1-1, ind2-1)
    
    
    left = fun(str1, str2, ind1-1, ind2)
    right = fun(str1, str2, ind1, ind2-1)

    return max(left, right)
    

str1 = 'f01e2d3e4'
str2 = 'f5e6d7e8'

ind1 = len(str1)
ind2 = len(str2)

out = fun(str1, str2, ind1-1, ind2-1)
print(out)



