n = 1


for i in range(n):
    for j in range(n-i):
        print(' ', end='')
        
    mul = 11**i
    temp = mul
    count = 0
    new_mul = ''
    
    while temp > 0:
        count += 1
        d = temp % 10
        new_mul += str(d) + ' '
        
        temp //= 10
          
    
    print(new_mul)    