
        
class Solution(object):
    def minTotal(triangle):
        if not triangle:
            return 0
        
        #start from second-to-last row and update the row above
        for i in range(len(triangle)-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1]) #sum with next level
                
        return triangle[0][0] #the top element contains the min path sum
        

   
'''range(len(triangle)-2, 0, -1) starts from len(triangle)-2 (the second-to-last row index) and goes down to 1 (exclusive), with a step size of -1. This means it would skip the first row (index 0) of the triangle.'''
  

