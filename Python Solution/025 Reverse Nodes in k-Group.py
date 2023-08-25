

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#d->1->2->3
#d->2->1->3
'''This approach involves reversing the nodes in groups of k as specified. Keep track of the current group's start and end nodes. Reverse the group, update the connections, and then move on to the next group.
'''

class Solution:
   def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        
        while True:
            group_start = prev_group_end.next
            group_end = group_start #init group end as start
            for i in range(k): #find group end
                if not group_end: #group end is null/empty --> reach end of list
                    return dummy.next
                group_end = group_end.next #move k step (0,1,...,k-1) to group end (end is 1 step ahead of reversed sublist)
            
            new_group_start = reverse_sublist(group_start, group_end)
            prev_group_end.next = new_group_start #link prev group to new group
            group_start.next = group_end #link new group end to next group start
            
            #update prev_group_end
            prev_group_end = group_start
            
        return dummy.next
            
   
   #reverse sublist
   def reverse_sublist(start, end):
        '''
        start: list start node
        end: the next node of list end node
        return: head of new reversed list
        '''
        prev, current = None, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev #new head of reverse list
    
  
