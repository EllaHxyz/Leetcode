class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: #check if prefix match head strings
                prefix = prefix[:-1] #shorten prefix to find
                if not prefix: #untill empty prefix
                    return "" #not found
        return prefix
        
   
    
'''The find() method finds the first occurrence index location of the specified value.
The find() method returns -1 if the value is not found. '''



    
