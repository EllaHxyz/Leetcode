

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def min_depth(self, root):
        if not root:
            return 0
        
        #if the node is a leaf, return 1 (the node itself)
        if not root.left and not root.right:
            return 1
        
        #if either left or right child is not present, calculate the depth of the present child
        if not root.left:
            return 1 + min_depth(root.right)
        if not root.right:
            return 1 + min_depth(root.left)
        
        # If both children are present, return the minimum depth of the two subtrees
        return 1 + min(min_depth(root.left), min_depth(root.right))
    
    
'''Height of an empty tree is 0'''
    
