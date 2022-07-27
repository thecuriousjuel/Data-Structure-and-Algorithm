def fun(s1, s2, ind1, ind2):
    #print(ind1, ind2)
    
    if ind1 < 0 or ind2 < 0:
        return 0
    
    if s1[ind1] == s2[ind2]:
        return 1 + fun(s1, s2, ind1-1, ind2-1)
    
    shift_ind1 = fun(s1, s2, ind1-1, ind2)
    shift_ind2 = fun(s1, s2, ind1, ind2-1)
    
    return max(shift_ind1, shift_ind2)



s1 = 'brute'
s2 = 'groot'

ind1 = len(s1)
ind2 = len(s2)

out = fun(s1, s2, ind1-1, ind2-1)

final = ind1+ind2-out
print(final)
