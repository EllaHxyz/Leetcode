
'''modified Binary Search'''
class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
         
            if nums[mid] == target:
                return True
            
            #Handle duplicates
            while left < mid and nums[left] == nums[mid]:
                left + = 1
            while right > mid and nums[right] == nums[mid]:
                right -= 1
                
            #binary search
            if nums[left] <= nums[mid]: #left part is sorted
                if nums[left] <= target < nums[mid]: #target is in the left part
                    #cut the search range to [left, mid-1]
                    right = mid - 1
                else: #target is in the right part
                    #cut search space to [mid+1, right]
                    left = mid + 1
                    
                
            else: #right part is sorted
                if nums[mid] < target <= nums[right]: #target is in the right part
                    left = mid + 1
                else: #target is in the left part
                    right = mid - 1
                    
        return False

