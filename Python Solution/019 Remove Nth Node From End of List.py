class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#e,g., n=2, head = 1-2-3-4-5 => 1-2-3-5

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = head
        
        for _ in range(n+1): #0, 1, ...n
            fast = fast.next
        
        while fast: #fast not NULL/empty
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next #remove Nth node
        
        return dummy.next
        

'''you can use the two-pointer approach. Maintain two pointers: one fast pointer that advances n+1 steps ahead of the slow pointer. Then move both pointers simultaneously until the fast pointer reaches the end of the list. At this point, the slow pointer will be pointing to the node right before the node that needs to be removed. Update the pointers to remove the node.'''

'''add a dummy head at the front, this is essential especially if the node to remove is the head node'''

