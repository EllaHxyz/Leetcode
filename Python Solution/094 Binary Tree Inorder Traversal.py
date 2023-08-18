'''recursion'''
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    #empty root
    if not root:
        return []
    
    #inorder recursion: Left-Node-Right
    result = []
    result += inorderTraversal(root.left)
    result.append(root.val)
    result += inorderTraversal(root.right)
    
    return result
    
'''Stack'''
def inorderTraversal_Stack(root):
    if not root:
        return []
    
    result = []
    stack = []
    current = root
    
    while current or stack:
        while current: #Traverse left subtree
            stack.append(current)
            current = current.left
            
        #Visit top node from stack
        current = stack.pop()
        result.append(current.val)
        
        #Traverse right subtree
        current = current.right
    
    return result
