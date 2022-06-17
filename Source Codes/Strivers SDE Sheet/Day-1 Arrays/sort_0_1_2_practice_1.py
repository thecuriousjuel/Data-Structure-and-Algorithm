zeros = 0
ones = 0
twos = 0

nums = [2,0,1]

for i in nums:
    if i == 0:
        zeros += 1
        
    if i == 1:
        ones += 1
        
    if i == 2:
        twos += 1
        
        
        
output = zeros * [0] + ones * [1] + twos * [2]

print(output)
