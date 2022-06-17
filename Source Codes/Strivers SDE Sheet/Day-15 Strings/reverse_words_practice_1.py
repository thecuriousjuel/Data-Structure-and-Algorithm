def reverse(string):
    string += ' '
    w = ''
    sen = ''
    
    for i in range(len(string)):
        if string[i] != ' ':
            w += string[i]
            
        else:
            
            sen = w + ' ' + sen 
            w = ''
            
    return sen
    
    
print(reverse('This is it'))