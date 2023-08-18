class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
def deleteDuplicates(head):
    #edge case: if empty linked list, then return itself
    if not head:
        return head
        
    current = head
    while current.next:
        if current.val == current.next.val:
                current.next = current.next.next
        else:
            current = current.next
    return head
        
        


