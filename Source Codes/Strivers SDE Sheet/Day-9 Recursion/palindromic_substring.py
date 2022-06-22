def is_palindromic(s):
    return s == s[::-1]


def p_substring(arr, out, ans):
    if len(arr) == 0:
        ans.append(out)
        return
    
    for i in range(1, len(arr)+1):
        if is_palindromic(arr[:i]):
            out.append(arr[:i])
            p_substring(arr[i:], out[:], ans)
            out.pop()
    
           
arr = 'aab'
index = 1
out = []
ans = []

p_substring(arr, out, ans)
print(ans)


