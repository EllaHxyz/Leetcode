class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        triplets = [] #no duplicate elements + sort ascd
        
        for i in range(len(nums) - 2):
            #skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #two pointers
            left, right = i+1, len(nums)-1 #left pointer to elements that come after the current element at index i
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0: #value < target = 0, move left pointer to right
                    left += 1
                elif total > 0: #value > target, move right pointer to left
                    right -= 1
                else: #value = target
                    triplets.append(nums[i], nums[left], nums[right])
                    
                    #continue to find other possible triplets
                    #skip duplicate
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    #update both left and right pointers; if only update one, the sum will not be 0 in this case
                    left += 1
                    right -= 1
        
        return triplets
   
    
'''you can use a two-pointer approach. First, sort the array. Then, iterate through the array and for each element, use two pointers to find the other two elements such that their sum equals the negation of the current element. Make sure to avoid duplicates and keep track of the unique triplets.'''
