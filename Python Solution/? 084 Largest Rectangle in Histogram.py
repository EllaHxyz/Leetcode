def largestRectangleArea(heights):
    '''
    :type heights: List[int]
    :rtype: int
    '''
    
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        
        stack.append(i)
    #
    while stack:
        
        
            
        

'''
stack - keep track of the indices of bars in ascending order of heights

In this implementation, we use a stack to keep track of the indices of the bars in ascending order of heights. As we iterate through the heights array, we check the current height against the height of the last bar in the stack. If the current height is less than the height of the last bar in the stack, it means we have found the right boundary of the rectangle formed by the last bar, and we can calculate the area of that rectangle.
'''



def largestRectangleArea(heights):
    stack = []
    max_area = 0

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)

        stack.append(i)

    # After processing all bars, calculate areas for any remaining bars in the stack
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)

    return max_area


