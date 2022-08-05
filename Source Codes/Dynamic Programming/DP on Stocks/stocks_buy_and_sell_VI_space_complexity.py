def fun(arr):    
    cur = [0 for _ in range(2)]
    nxt = [0 for _ in range(2)]
    
    for ind in range(len(arr)-1, -1, -1):
        cur[1] = max(-arr[ind] + nxt[0], 0 + nxt[1])
        cur[0] = max(-fee + arr[ind] + nxt[1], 0 + nxt[0])
        
        nxt = cur
        
    return cur[1]


price = [4,9,0,4,10]
ind = 0
buy = 1
fee = 2

out = fun(price)
print(out)



