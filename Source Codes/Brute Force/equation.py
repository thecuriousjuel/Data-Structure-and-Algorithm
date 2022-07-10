def fun():
    i = 0
    j = 0
    
    for i in range(100):
        for j in range(100):
            if i+j == 10 and 3*i+5*j == 42:
                return i, j
            
            if i+j > 10 or 3*i+5*j > 42:
                break
            
    return None, None


x, y = fun()

print(f'x={x}, y={y}')
