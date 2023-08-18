
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = None
        
    def recoverTree(self, root):
        #perform inorder traversal
        self._in_order_traversal(root)
        # Swap the values of the two misplaced nodes
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def _in_order_traversal(self, node):
            if not node:
                return
            
            #in-order traversal:left
            self._in_order_traversal(node.left)
            
            #visit current node
            #check if the current node is greater than the next node
            if self.prev and self.node.val < self.prev.val:
                #detect wrong order -> record them to first and second
                if not self.first:
                    self.first = self.prev
                    self.second = node
                else:
                    self.second = node
            
            #update prev
            self.prev = node
            
            #in_order traversal: right
            self._in_order_traversal(node.right)
            
  
