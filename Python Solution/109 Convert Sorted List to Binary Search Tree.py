
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        
        #Find the middle node using slow and fast pointers
        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        #Disconnect the left part from the middle node
        if prev:
            prev.next = None
        else:
            head = None
        # Create the root node using the middle node value
        root = TreeNode(slow)
        
        #Recursively build the left and right subtrees
        root.left = sortedListToBST(head)
        root.right = sortedListToBST(slow.next)
        
        return root
        
    
    
