class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {')':'(',
                        '}':'{',
                        ']':'['
                      }
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map.keys():
                if not stack or bracket_map[char] != stack.pop(): #stack is empty or no match found
                    return False
                #match found - no action needed, match already popped from stack
            else: #non valid elements
                return False
                
        
        return not stack #stack is empty - match found


