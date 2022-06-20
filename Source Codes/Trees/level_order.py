from BinarySearchTree import bst


def level_order(root):
    queue = [root]
    
    while len(queue) > 0:
        
        node = queue[0]
        
        print(node.data, end = ' ')
        
        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)

        queue = queue[1:]


level_order(bst.root)


