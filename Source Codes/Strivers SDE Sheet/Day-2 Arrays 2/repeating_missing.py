array = [3,1,2,5,3]

my_dict = {}

for i in range(1, len(array) + 1):
    my_dict[i] = 0
    
A = None
B = None

    
for i in range(1, len(array) + 1):    
    my_dict[array[i-1]] += 1
    
    if my_dict[array[i-1]] == 2:
        A = array[i-1]
        
    
for i in my_dict:
    if my_dict[i] == 0:
        B = i
        
print(A, B)
        
    
