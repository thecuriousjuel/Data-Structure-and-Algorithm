matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]

target = 61
found = False

for i in matrix:
    if i[0] <= target <= i[-1]:
        for j in range(len(i)):
            if i[j] == target:
                found = True
                
                
print(found)
