string = '[{'

open = '[{('
close = ']})'

temp = ''
flag = 0

if len(string) == 1 and string[0] in close:
    print('Not Balanced')
else:
    for i in string:
        if i in open:
            temp += i
        
        if i in close:
            if temp[-1] == open[close.index(i)]:
                temp = temp[:-1]
            else:
                flag = 1
                break
            
    if flag == 0 and len(temp) == 0:
        print('Balanced')
    else:
        print('Not Balanced')
