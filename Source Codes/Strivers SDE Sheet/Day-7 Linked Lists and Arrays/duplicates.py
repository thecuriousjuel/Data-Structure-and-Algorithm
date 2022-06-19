arr = [1,1,2,2,2,3,3]

my_dict = {}

for i in arr:
    my_dict[i] = 0
    
    
for i in arr:
    my_dict[i] += 1
    
    
arr = list(my_dict.keys())
output = len(arr)

print(arr, output)
