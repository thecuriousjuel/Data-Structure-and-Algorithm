def fun(s, t, ind1, ind2):
    
    if ind1 < 0 and ind2 < 0:
        return True
    
    if ind2 < 0 or ind1 < 0:
        return False

    if s[ind1] == t[ind2]:
        return fun(s, t, ind1-1, ind2-1)

    return fun(s, t, ind1, ind2-1)
      
s = ''
t = 'ahbgdc'


ind1 = len(s)-1
ind2 = len(t)-1
        
out = fun(s, t, ind1, ind2)
print(out)





