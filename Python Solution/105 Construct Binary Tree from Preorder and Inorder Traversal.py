
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def buildTree(preorder, inorder):
    
        if not preorder or not inorder:
            return None
        
        #the first element of preorder is the root value
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        #find the position of the root in inorder
        root_idx = inorder.index(root_val) #index of first occurrence
        
        #recursively build the left and right subtrees
            #root idx of inorder divide the preorder list to left and right tree
            #root of preorder (first num) divide the inorder list to left and right tree
        root.left = buildTree(preorder[1:1+root_idx], inorder[:root_idx])
        root.right = buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        
        return root
    
    
    
    
    
