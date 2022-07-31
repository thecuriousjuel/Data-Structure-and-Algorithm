def fun(s1, s2, i, j):
    
    if i < 0:
        return j+1
    
    if j < 0:
        return i+1
    
    if s1[i] == s2[j]:
        return fun(s1, s2, i-1, j-1)
        
    
    insert = 1 + fun(s1, s2, i, j-1)
    remove = 1 + fun(s1, s2, i-1, j)
    update = 1 + fun(s1, s2, i-1, j-1)
    
    return min(insert, remove, update)



s1 = 'horse'
s2 = 'ros'

n = len(s1)
m = len(s2)

out = fun(s1, s2, n-1, m-1)
print(out)

