# Not correct

def display(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print()
        

def fun(arr, ind, t, dp, path=[]):
    if ind == len(arr):
        if t == 0:
            print(path)
            return 1
        return 0
    
    print(ind, t)
    
    if dp[ind][t] != '-':
        return dp[ind][t]
    
    path.append('+')
    plus = fun(arr, ind+1, t-arr[ind], dp, path)
    path.pop()
    path.append('-')
    
    minus = fun(arr, ind+1, t+arr[ind], dp, path)
    path.pop()
    
    dp[ind][t] = plus + minus
    
    return dp[ind][t]
    
    
arr = [1,2,3,1]
target = 3

temp = sum(arr) + target

dp = [['-' for _ in range(temp+1)] for _ in range(len(arr))]

out = fun(arr, ind=0, t=target, dp=dp)

display(dp)
print(out)


