
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    
    def levelOrderBottom(self, root):
        if not root:
            return []
        result = []
        queue = [root] #store node to traverse
        
        while queue:
            level_values = []
            
            for i in range(len(queue)):
                node = queue.pop(0)
                level_values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            #insert later level values to top of result
            result.insert(0, level_values)
        
        return result
  
