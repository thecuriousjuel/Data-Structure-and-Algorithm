def fun(cost, ind):
    
    if ind == 0:
        return cost[ind]
    
    if ind < 0:
        return 0

    one_step = cost[ind] + fun(cost, ind-1)

    two_step = cost[ind] + fun(cost, ind-2)
    
    return min(one_step, two_step)


cost = [10,15,20]
ind = len(cost)

out1 = fun(cost, ind-1)
out2 = fun(cost, ind-2)

print(min(out1, out2))

    
    