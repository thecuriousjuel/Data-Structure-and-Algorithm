def palindrome(string, l, r):
    if l >= r:
        return True

    if string[l] != string[r]:
        return False

    return palindrome(string, l+1, r-1)
    

string = '1221'
print(palindrome(string, 0, len(string) - 1))

