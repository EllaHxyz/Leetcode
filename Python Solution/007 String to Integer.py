class Solution(object):
    def myAtoi(self, s):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.strip() #remove leading and trailing spaces
        
        if not s: #s is empty
            return 0
        
        #determine sign of number
        sign = 1
        i=0
        if s[i] in '+-':
            sign = 1 if s[i] == '+' else -1
            i += 1
        
        num=0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i]) #convert str to int
            
            num = num * 10 + digit #update num
            i += 1 #update index
            
            #handle overflow
            if num > INT_MAX:
                return INT_MAX if sign == 1 else INT_MIN
        
            if num > (INT_MAX - digit)
    
        return num*sign
'''

The isdigit() method returns True if all the characters are digits, otherwise False.

a digit is a character that has the property value Numeric_Type=Digit or Numeric_Type=Decimal.

Special cases:
1. Exponents, like ², are also considered to be a digit.
2. The isdigit() method considers unicode representation of numbers as digits only.
3. The fractions are not considered as digits. So, if the created string contains fractions in unicode format or any other format, the method returns false.

a = "\u0030" #unicode for 0 -> True
b = "\u00B2" #unicode for ² -> True
str = "\u00BE" #unicode for fraction 3/4 -> False
'''

