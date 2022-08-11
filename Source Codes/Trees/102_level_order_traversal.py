from bst_hardcoded import bst1

# Performed preorder
def fun(bst1, llist):
    if bst1 != None:
        llist.append(bst1.data)
        fun(bst1.left, llist)
        fun(bst1.right,llist)
        
        
llist = []
fun(bst1, llist)
print(llist)