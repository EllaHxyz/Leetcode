class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        quadruplets = []
        
        for i in range(len(nums) - 3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                #skip duplicates
                if j> i+1 and nums[j] == nums[j-1]:
                    continue
                    
                #init pointers
                left, right = j+1, len(nums) - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else: #total = target
                        quadruplets.apend(nums[i], nums[j], nums[left], nums[right])
                        #update pointers
                        
                        #skip duplicate
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        #move left and right inward
                        left += 1
                        right -= 1
                    
'''you can use a similar approach to the 3Sum problem. Sort the array, and then use nested loops to fix two elements and find the other two elements using two-pointer technique.'''
