'''recursion with backtracking'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self._generateTrees(1, n)
    
    #Helper Function
    def _generateTrees(self, start, end):
        #base case: return an empty subtree
        if start > end:
            return [None]
        
        all_trees = []
        #let root = i
        for i in range(start, end+1):
            left_subtrees = self._generateTrees(start, i-1)
            right_subtrees = self._generateTrees(i+1, end)
            
            #for base case, construct the tree root node with null left and null right subtree.
            for left_tree in left_subtrees:
                for right_tree in right_subtrees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)
        return all_trees
 
