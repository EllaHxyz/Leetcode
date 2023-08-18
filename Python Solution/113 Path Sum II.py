

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def PathSum(self, root, sum):
        result = []
        self._dfs(root, sum, [], result)
        return result
        
        
    def _dfs(self, root, sum, path, result):
        
        if not root:
            return
        
        #check if leaf node = sum; if yes, add path to result
        if not root.left and not root.right:
            if root.val == sum:
                #path.append(root.val) #update path
                result.append(path) #add curr path to result
        
        
        #recursion to check left and right child
        sum -= root.val #update sum
        #path.append(root.val) #update path
        self._dfs(root.left, sum, path, result)
        self._dfs(root.right, sum, path, result)
    
