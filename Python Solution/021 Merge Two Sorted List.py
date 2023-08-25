class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode() # create a dummy node
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next #update current
        
        #attach remaining nodes if any - all at once
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        
        return dummy.next
        
   '''you can create a new linked list and iterate through the input linked lists while comparing their nodes. Append the smaller node to the new list and move the corresponding pointer in that linked list forward. Repeat this process until you've traversed both input lists.'''
   '''In the beginning, dummy and current points to the same node - ListNode()'''
   
