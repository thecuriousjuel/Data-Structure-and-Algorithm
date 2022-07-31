def fun(str1, str2, ind1, ind2):
    if ind2 < 0:
        return 1
    
    if ind1 < 0:
        return 0
    
    if str1[ind1] == str2[ind2]:
        return fun(str1, str2, ind1-1, ind2-1) + fun(str1, str2, ind1-1, ind2)
    
    return fun(str1, str2, ind1-1, ind2)
    


str1 = 'rabbbit'
str2 = 'rabbit'

ind1 = len(str1)
ind2 = len(str2)

out = fun(str1, str2, ind1-1, ind2-1)
print(out)

