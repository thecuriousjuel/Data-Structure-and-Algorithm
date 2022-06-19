N = 7
nums = [2,2,1,1,1,2,2]

count = {}


for i in nums:
    count[i] = 0
    

for i in nums:
    count[i] += 1
    

n = N // 3

for i in count:
    if count[i] > n:
        print(i)
        break
    
    