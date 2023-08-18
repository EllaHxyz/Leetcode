


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        mid = len(nums) // 2 #integer division
        root = TreeNode(nums[mid])
        
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid + 1:])
    
    return root
        
        
    
