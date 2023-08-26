

class Solution:
    def removeElement(self, nums, val):
        new_length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[new_length] = nums[i]
                new_length += 1
            elif nums[i] == val:
                continue
        return new_length
        
        
   
   

