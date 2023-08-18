
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        
        #base case
        if not root:
            return 0
        
        #recursion: maxDepth = max(maxDepth-left, maxDepth-right)+1
        return max(maxDepth(root.left), maxDepth(root.right))+1
