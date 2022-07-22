def fun(arr, ind, target, dp):
    
    if target == 0:
        return True
    
    if ind == 0:
        return arr[ind] == target
    
    if dp[ind][target] != -1:
        return dp[ind][target]
 
    not_take = fun(arr, ind-1, target, dp)
    
    take = False
    if arr[ind] <= target: 
        take = fun(arr, ind-1, target-arr[ind], dp)
        
    dp[ind][target] = not_take or take
    
    return dp[ind][target]



def display(dp):
    
    print('\t', end=' ')
    for i in range(len(dp[0])):
        print(i, end='\t')
    print()
    
    for i in range(len(dp)):
        print(i, end='\t')
        for j in range(len(dp[i])):
            print(dp[i][j], end='\t')
        print()
        


def array_check(arr):
    n = len(arr)
    s = 0
    
    for i in arr:
        s += i

    if s % 2 != 0:
        return False
    
    target = s // 2
    
    dp = [[-1 for _ in range(target+1)] for _ in range(n)]

    out = fun(arr, n-1, target, dp)
    
    display(dp)

    return out

arr = [1,2,3,4,1,2,1]
print('Final : ', array_check(arr))




