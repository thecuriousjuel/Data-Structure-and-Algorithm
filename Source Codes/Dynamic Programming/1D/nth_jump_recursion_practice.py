def fun(ind):
    if ind <= 1:
        return 1
    
    one_step = fun(ind-1)
    two_step = fun(ind-2)
    
    return one_step + two_step


print(fun(4))