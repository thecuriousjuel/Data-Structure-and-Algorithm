arr1 = [1, 4, 8, 10]
arr2 = [2, 3, 9]

new_arr = []

while len(arr1) > 0 and len(arr2) > 0:
    
    if arr1[0] < arr2[0]:
        new_arr.append(arr1[0])
        arr1 = arr1[1:]
        
    else:
        
        new_arr.append(arr2[0])
        arr2 = arr2[1:]
        
if len(arr1) > len(arr2):
    new_arr.extend(arr1)
else:
    new_arr.extend(arr2)
    
print(new_arr)