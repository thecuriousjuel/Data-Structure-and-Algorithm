def fun(str1, str2, ind1, new_str):
    
    if ind1 == len(str1):
        if new_str == str2:
            print(new_str)
        return ''

    
    new_str += str1[ind1]
    pick = str1[ind1] + fun(str1, str2, ind1+1, new_str)
    new_str = new_str[:-1]
    
    not_pick = '' + fun(str1, str2, ind1+1, new_str)

    return max(pick, not_pick)


str1 = 'babgbag'
str2 = 'bag'

ind1 = len(str1)

fun(str1, str2, ind1=0, new_str='')
