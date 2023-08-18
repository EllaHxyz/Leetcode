class Solution(object):
    def longestPalindrome(self, s):
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right] # = slice [left+1, right-1]
        
        longest = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i,i)
            even_palindrome = expand_around_center(i, i+1)
            
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrom) > len(longest):
                longest = even_palindrom
        return longest

'''To solve this problem, you can use the concept of expanding around centers. For each character in the string, consider it as the center of a potential palindrome and expand outwards to check if the characters around the center form a palindrome. Repeat this process for both odd-length and even-length palindromes.'''
