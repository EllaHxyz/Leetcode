class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        
        reverse_num = 0
        sign = 1 if x > 0 else -1 #handle sign +-
        x = abs(x)
        
        while x != 0:
            pop = x % 10
            x //= 10
            reverse_num = reverse_num*10 + pop
            
            #overflow
            if reverse_num > INT_MAX:
                return 0 #if overflow, return 0
        
        return reverse_num * sign
        
   
