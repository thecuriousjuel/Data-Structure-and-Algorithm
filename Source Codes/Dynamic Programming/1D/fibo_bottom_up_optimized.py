n = 5
count = 0

a = 0
b = 1
c = 0


while count < n:
    c = a + b
    b = a
    a = c

    count += 1
    
print(c)



