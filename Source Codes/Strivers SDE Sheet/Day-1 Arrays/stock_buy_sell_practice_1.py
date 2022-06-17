prices = [7,1,5,3,2,4]


max_prices = 0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        max_prices = max(prices[j]-prices[i], max_prices)
        
print(max_prices)