N = 10
nums = [4,4,2,4,3,4,4,3,2,4]

count = {}


for i in nums:
    count[i] = 0
    

for i in nums:
    count[i] += 1
    

n = N // 2

for i in count:
    if count[i] > n:
        print(i)
        break
    
    