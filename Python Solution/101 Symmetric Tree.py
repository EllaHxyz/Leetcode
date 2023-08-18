
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        def is_mirror(self, left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)
            
        return is_mirror(root, root)
