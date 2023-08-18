class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
def deleteDuplicatesII(head):

    #edge case: if empty linked list, then return itself
    if not head:
        return head
    
    dummy = ListNode()
    dummy.next = head
    prev, curr = dummy, head
    
    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
        
    return dummy.next
    
'''because both prev and dummy refer to the same object in memory. Any modifications made through prev will be reflected in dummy.'''
    
'''Here's how the prev pointer works in the context of the solution:

Initialize prev to the dummy node: prev = dummy. The dummy node is introduced at the beginning to handle edge cases, and prev initially points to the dummy node.

Traverse the linked list with the curr pointer: curr = head. The curr pointer is used to traverse the linked list, starting from the head node.

Skip all duplicate nodes: The algorithm uses a while loop to skip all duplicate nodes. If curr has duplicates, the loop will continue until curr points to the last duplicate node.

Update prev.next to the next distinct node: Once the loop finds the last duplicate node, the prev.next reference is updated to skip all the duplicate nodes, and it now points to the next distinct node in the linked list.

Move prev to the next distinct node: After updating prev.next, the prev pointer is moved to the next distinct node so that it is ready to update its next reference if another group of duplicates is encountered.

The key role of prev = prev.next is to move the prev pointer forward to the next distinct node after all duplicate nodes have been skipped. This ensures that prev always points to the previous distinct node, which is essential for correctly modifying the next references in the linked list.

By the end of the algorithm, the prev pointer will have traversed the linked list, skipping all duplicate nodes and linking only the distinct nodes together, resulting in the modified linked list with duplicate nodes removed.

'''
