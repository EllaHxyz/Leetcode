
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        return is_valid_helper(root, float('-inf'), float('inf'))
    
    def is_valid_helper(node, lower_bound, upper_bound):
        
        #base 1: check all the way, no invalid found
        if not node:
            return True
        
        #base 2: invalid node - value out of bound
        if node.val <= lower_bound or node.val >= upper_bound:
            return False
        
        #recursive check left and right subtree with updated bounds
        return (is_valid_helper(node.left, lower_bound, node.val) and is_valid_helper(node.right, node.val, upper_bound))
  
