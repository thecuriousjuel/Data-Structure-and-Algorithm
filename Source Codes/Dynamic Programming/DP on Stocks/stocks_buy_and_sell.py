def fun(arr):
    profit = 0
    mini = arr[0]
    
    for i in range(1, len(arr)):
        price = arr[i] - mini
        profit = max(price, profit)
        mini = min(mini, arr[i])
        
    return profit
       
arr = [7, 1, 5, 3, 6, 10]

out = fun(arr)

print(out)
        