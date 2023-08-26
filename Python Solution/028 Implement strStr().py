

class Solution:
    def strStr(haystack, needle):
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        #empty needle
        if not needle:
            return 0
            
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
    
    
   
   
   

