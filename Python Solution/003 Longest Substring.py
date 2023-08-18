class Solution(object):
def lengthOfLongestSubstring(self, s):

    '''
    Find the longest substring in s, without repeatition.
    Return the length.
    
    :type s: str
    :rtype: int
    '''
    #create a dict to store the index of each character seen so far
    char_index = {} #{ch: index}
    max_length = 0
    left = 0 #left pointer of the sliding window
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            #update left pointer to next position
            left = char_index[s[right]] + 1
        else:
            #if new character, or its previous occurrence is not in the current window
            #update max length
            max_length = max(max_length, righ - left +1)
        #update dict
        char_dict[s[right]] = right
    
    return max_length
        
  
