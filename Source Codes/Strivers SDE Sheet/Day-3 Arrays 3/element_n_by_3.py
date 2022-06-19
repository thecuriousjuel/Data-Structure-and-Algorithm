nums = [10,20,40,40,40]
N = len(nums)

count = {}


for i in nums:
    count[i] = 0
    

for i in nums:
    count[i] += 1
    

n = N // 3

for i in count:
    if count[i] > n:
        print(i)

    
    
