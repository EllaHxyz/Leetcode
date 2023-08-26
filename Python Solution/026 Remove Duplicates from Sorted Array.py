

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        unique_index = 1 #start at the second element
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_index] = nums[i]
                unique_index += 1 #update index
                
        return unique_index #num of uniqe elements
        
        '''you can use two pointers to keep track of the current position in the original array and the position where the next unique element should be placed. As you iterate through the array, whenever you encounter a new element, you move it to the next position in the array, effectively eliminating duplicates.'''
        
                
   

