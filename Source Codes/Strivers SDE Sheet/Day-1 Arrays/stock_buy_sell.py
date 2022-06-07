prices = [7,6,4,3,1]
price_diff = float('-inf')

for i in range(len(prices)):
    for j in range(i, len(prices)):
        if prices[j] - prices[i] > price_diff:
            price_diff = prices[j] - prices[i]


if price_diff == float('-inf'):
    print(0)
else:
    print(price_diff)