
        
class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        
        #init first row
        pre_row = [1]
        
        for i in range(1, rowIndex+1):
            new_row =[1] #first element is 1
            
            for j in range(1, i):
                new_row.append(pre_row[j-1] + pre_row[j])
            new_row.append(1) #last element is 1
            
            pre_row = new_row #update pre_row
        
        return pre_row
        
        
        
  

