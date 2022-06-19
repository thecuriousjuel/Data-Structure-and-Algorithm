arr = [3,1,3,4,2]

my_dict = {}

for i in arr:
    my_dict[i] = 0
    
for i in arr:
    my_dict[i] += 1
    if my_dict[i] == 2:
        print(i)
        break