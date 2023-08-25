

import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(lists):
        heap =[]
        
        #Initialize the heap with the first node from each list
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i))
                lists[i] = lst.next
        
        dummy = ListNode() # Dummy node to simplify insertion
        current = dummy
        
        while heap:
            val, index = heapq.heappop(heap)
            current.next = ListNode(val)
            current = current.next
             
            if lists[index]:
                heapq.heappush(heap, (lists[index].val, index))
                lists[index] = list[index].next
        
        return dummy.next
                
