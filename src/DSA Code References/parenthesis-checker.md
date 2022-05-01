```python
def ispar(x):
        
    stack = []

    start_sym = '[{('
    end_sym = ']})'

    for i in x:
    #     print(stack, i)
        if i in start_sym:
            stack.append(i)
        elif i in end_sym:
    #         print(f'{end_sym[start_sym.index(stack[-1])]} == {i}')
            if not stack:
                return False


            if end_sym[start_sym.index(stack[-1])] == i:
                stack.pop()
            else:
                return False

    if stack:
        return False

    return True
```


```python
ispar('(')
```




    False




```python

```
