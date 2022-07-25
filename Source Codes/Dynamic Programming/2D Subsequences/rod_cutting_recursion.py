def fun(price, ind, N):
    
    if N == 0:
        return 0
    
    if ind == len(price):
        return float('-inf')
    
    pick = float('-inf')
    if N-(ind+1) >= 0:   
        pick = price[ind] + fun(price, ind+1, N-(ind+1))
    not_pick = 0 + fun(price, ind+1, N)

    return max(pick, not_pick)


price = [2,5,7,8,10]

N = 5

out = fun(price, ind=0, N=N)

print(out)



