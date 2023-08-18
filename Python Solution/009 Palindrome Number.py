class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        
        reverse_num=0
        original_x = x
        
        while x != 0:
            pop = x % 10 #last digit
            x //= 10 # x remove last digit
            
            reverse_num = reverse_num * 10 + pop
        
        return reverse_num = original_x
        

'''To solve this problem, you can reverse the digits of the integer and then compare the reversed integer with the original integer. If they are the same, then the integer is a palindrome.'''

