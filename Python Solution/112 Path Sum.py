

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        
        #check if leaf node = sum; update sum for each recursion
        if not root.left and not root.right:
            return root.val == sum
        
        #recursion to check left and right child
        sum -= root.val #update sum
        return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

d
