
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def buildTree(inorder, postorder):
        if not inorder or not postorder:
            return None
        root_val = postorder[-1]
        root_idx = inorder.index(root_val) #this index will divide postorder to                                     left and right
        root = TreeNode(root_val)
        root.left = buildTree(inorder[:root_idx], postorder[:root_idx])
        root.right = buildTree(inorder[root_idx+1:], postorder[root_idx:-1])
    
        
    
    
