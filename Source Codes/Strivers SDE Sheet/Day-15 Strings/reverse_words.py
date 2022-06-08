words = 'this is an amazing program'
words += ' '
w = ''
s = ''

for i in range(len(words)):
    if words[i] != ' ':
        w += words[i]
    else:
        s = w + ' ' + s
        w = ''

s = s[:-1]
print(s)
