

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def is_balanced(self, root):
        def check_height(node):
            #base case: empty node -> height=-1
            if not node:
                return 0
            left_height = check_height(node.left)
            right_height = check_height(node.right)
            
            #check if left and right subtrees differ in heigh by no more than 1
            if abs(left_height - right_height) >1:
                return -1 #-1 indicate unbalanced tree
                
            #return the height of current node
            return 1+max(left_height, right_height)
            
    return check_height(root) != -1

'''Note: The height of an empty tree is 0'''
  
        
    
    
