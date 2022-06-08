b_open = '({['
b_close = ')}]'

data = '{[]()}'
stack = []
i = 0
flag = 0

while i < len(data):
    if i == 0 and data[i] in b_close:
        flag = 1
        break

    if data[i] in b_open:
        stack.append(data[i])

    elif data[i] in b_close:
        if len(stack) == 0:
            flag = 1
            break
        
        j = b_open.index(stack[-1])
        if data[i] != b_close[j]:
            flag = 1
            break
        else:
            stack.pop()

    i += 1

if flag == 0 and len(stack) == 0:
    print(True)
else:
    print('False')

        

