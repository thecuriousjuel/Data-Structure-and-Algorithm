from bst_hardcoded import bst3

def fun(root, B, llist):
    if root:
        llist.append(root.data)
    
        if root.data == B:
            return True
        
        left = fun(root.left, B, llist)
        right = fun(root.right, B, llist)
        
        if left or right:
            return True
        
        llist.pop()
        
    return False


list1 = []
fun(bst3, 5, list1)
print(list1)

list2 = []
fun(bst3, 1, list2)
print(list2)

i = 0
out = None

while i < len(list1) and i < len(list2):
    if list1[i] == list2[i]:
        out = list1[i]
    
    i += 1
        
print(out)
        



