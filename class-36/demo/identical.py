class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def identical(tree1, tree2):

    # If both trees are empty -> return True
    if tree1 is None and tree2 is None:
        return True
    
    # If both trees are non empty
    if tree1 is not None and tree2 is not None:
        # compare
        if tree1.data == tree2.data:
            if identical(tree1.left, tree2.left) and identical(tree1.right, tree2.right):
                return True 
            
    # If one of the trees is empty and the other is not        
    return False

root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)
root1.left.right = Node(4)
root1.right.right = Node(6)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.right = Node(4)
root1.right.right = Node(6)

print(identical(root1,root2))
