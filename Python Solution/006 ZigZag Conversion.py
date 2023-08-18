class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        result = ['']*numRows #return ['','',''] to represent 3 rows
        index, step = 0,1
        
        for char in s:
            result[index] += char
            
            if index = 0:
                step = 1
            elif index = numRows - 1:
                step = -1
            
            index += step
            
        return ''.join(result) #he join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator. e.g., '#'.join(list)
            
        
    

'''To solve this problem, you can simulate the process of filling the zigzag pattern rows by row. Keep track of the characters in each row and their positions based on the zigzag pattern.'''
