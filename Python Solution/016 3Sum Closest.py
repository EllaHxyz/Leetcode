class Solution(object):
    def threeSum(self, nums, target):
        
        nums.sort()
        res = 0
        min_dist = pow(2, 31)-1
        
        for i in range(len(nums) - 2):
            
            #two pointers
            left, right = i+1, len(nums)-1 #left pointer to elements that come after the current element at index i
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                #determine min_dist, store results
                idist = abs(total - target)
                if dist < min_dist:
                    res = total
                    min_dist = dist
                
                if total < target: #value < target, move left pointer to right
                    left += 1
                elif total > target: #value > target, move right pointer to left
                    right -= 1
                else: #value = target
                    return target
        
        return res
   
