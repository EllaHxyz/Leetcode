

        
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
            
        leftmost = root #leftmost will always point to the most left point of each level
        while leftmost.left:
            #start from leftmost point,
            #traverse across this level
            curr = leftmost
            while curr:
                #connect curr's childs
                curr.left.next = curr.right #point left child to right child
                if curr.next:
                    curr.right.next = curr.next.left #point right child to next's left child
                #update curr to its next
                curr = curr.next
            
            #update leftmost to its left child
            leftmost = leftmost.left
        
        return root
        
            
