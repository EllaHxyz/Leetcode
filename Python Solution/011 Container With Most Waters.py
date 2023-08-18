class Solution(object):
    def MaxArea(height):
        max_area= 0
        left, right = 0, len(height) - 1
        
        while left < right:
            #calculate max area
            h = min(height[left], height[right]) #shorter one
            w = right - left
            area = h*w
            max_area = max(max_area, area)
        
            #update pointers - only update the one points to shorter height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
'''you can use a two-pointer approach. Start with two pointers at the beginning and end of the array. Calculate the area between the walls represented by the pointers, and then move the pointers inward while updating the maximum area.'''
