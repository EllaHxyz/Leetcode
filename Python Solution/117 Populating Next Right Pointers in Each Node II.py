

        
class TreeNode:
    def __init__(self, val, left=None, right=None, next=None)
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
class Solution(object):
    def connect(root):
        if not root:
            return root
        
        leftmost = root
        
        while leftmost: #if child leftmost exist, move to the child level
            curr = leftmost #node at the current traversal level
            prev = None #the child node waiting to be connected
            leftmost = None #the leftmost node at the child level
            
            #traverse all node in the curr level
            while curr:
                if curr.left: #check left child
                    if not leftmost:
                        leftmost = curr.left #assign LM
                    if prev:
                        prev.next = curr.left #connect prev to left child
                    prev = curr.left #assign prev to left child
                if curr.right: #check right child
                    if not leftmost:
                        leftmost = curr.right
                    if prev:
                        prev.next = curr.right
                    prev = curr.right
                #update curr to its next (on the same level)
                curr = curr.next
        return root
                
                
