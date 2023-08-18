class Solution(object):
    def romanToint(self, s):
        roman_to_int = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
        }
        
        total = 0
        prev_value = 0
        
        for symbol in s:
            value = roman_to_int[symbol]
            
            if value > prev_value:
                total += value - 2*prev_value
            else:
                total += value
            
            prev_value = value
        return total
        
    
