def fun(string, ind, s=''):
    
    if ind == len(string):
        print(s)
        return
    
    s+=string[ind]
    fun(string, ind+1, s)
    
    s = s[:-1]
    fun(string, ind+1, s)


string = 'abc'
fun(string, ind=0)

