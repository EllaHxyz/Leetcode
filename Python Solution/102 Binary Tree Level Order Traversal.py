
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        result = []
        if not root:
            return result
        curr_level = [root]
        while curr_level:
            level_result =[]
            next_level = []
            for node in curr_level:
                level_result.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(level_result)
            curr_level = next_level
        return result
