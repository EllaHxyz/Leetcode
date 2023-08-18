
        
class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
            
        #init with first row
        triangle = [[1]]
        
        for i in range(1, numRows):
            prev_row = triangle[i-1]
            new_row = [1] #first element of the row is always 1
            
            for j in range(1, i):
                new_row.append(prev_row[j-1]+prev_row[j]) #calculate element by add the two above elements
                
            new_row.append(1) #last element of the row is always 1
            triangle.append(new_row)
        
        return triangle
    
