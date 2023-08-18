class ListNode:
    #init: default val as 0!
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def addTwoNumbers(l1, l2):
        '''
        :type l1,l2: ListNode
        :rtype: ListNode
        '''
        dummy = ListNode()
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            #calculate the sum
            total_sum = carry
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next
            #update carry
            carry = total_sum // 10 #Integer division returns the quotient of the                       division without the remainder.
            #create a new node for the result
            current.next = ListNode(total_sum % 10)
            #update current
            current = current.next
        
        #return w/o leading 0:
        return dummy.next
'''
Here are some common rules for determining the truthiness or falsiness of objects in Python:
All non-empty objects are considered truthy. For example, a non-empty string, list, tuple, dictionary, or any custom object is truthy.
Empty objects are considered falsy. For example, an empty string, list, tuple, dictionary, or any custom object with no attributes or elements is falsy.
Numeric objects are truthy if their value is non-zero, and falsy if their value is zero.
None, False, and numeric zero (e.g., 0, 0.0, 0j) are explicitly falsy.
'''


