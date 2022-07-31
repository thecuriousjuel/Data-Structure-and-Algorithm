def fun(str1, str2, ind1, ind2):
    
    if ind1 < 0 and ind2 < 0:
        return True
    
    if ind1 < 0 and ind2 >= 0:
        return False

    if ind2 < 0 and ind1 >= 0:
        for i in range(ind1, 0, -1):
            if str1[i] != '*':
                return False
        return True

    if str1[ind1] == str2[ind2] or str1[ind1] == '?':
        return fun(str1, str2, ind1-1, ind2-1)

    if str1[ind1] == '*':
        left = fun(str1, str2, ind1-1, ind2)
        right = fun(str1, str2, ind1, ind2-1)
        
        return left or right

    return False


str1 = 'ab*cd'
str2 = 'abcdefcd'

ind1 = len(str1)
ind2 = len(str2)

out = fun(str1, str2, ind1-1, ind2-1)
print(out)



