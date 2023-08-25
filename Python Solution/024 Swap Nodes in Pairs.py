

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#d->1->2->3
#d->2->1->3

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        #swap
        while current.next and current.next.next: #not null
            node1 = current.next
            node2 = current.next.next
            node3 = current.next.next.next
            
            #swap
            current.next = node2
            node2.next = node1
            node1.next = node3
            
            #update current
            current = current.next.next
            
        return dummy.next
        
'''
def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        
        # Swapping nodes
        first.next = second.next
        second.next = first
        current.next = second
        
        current = current.next.next  # Move to the next pair
    
    return dummy.next
'''
