

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def flatten(self, root):
        stack = []
        while root:
            #has left ->flip tree (put right tree to stack before set to None)
            if root.left:
                if root.right:
                    stack.append(root.right)
                root.right, root.left = root.left, None
            #till right becomes empty, but has stack
            if not root.right and stack:
                #pull node from stack, add to right
                root.right = stack.pop()
            #move
            root = root.right

'''
    while root is not None:
    
    if left exists?

    yes-> if right exist?
            yes -> put right tree to stack before set it to None
          flip left tree to right, and set right to None
    
    no -> if right child is empty but stack non-empty?
            yes -> pop node from stack, add to right child
            
    update root to its right child, and repeat.
'''
