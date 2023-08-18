class Solution(object):
# 1. Backtracking
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        digit_to_letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
        }
        
        result = []
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in digit_to_letters[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
        
        backtrack("", digits)
        
        return result #list of strings
    
# 2. DFS
    def letterCombine(self, digits):
        if not digits:
            return []
        result = []
        self.dfs("", digits, result)
        return result
    
    def dfs(self, combination, digits, result):
        if not digits:
            result.append(combination)
        for letter in letter2digits[digits[0]]:
            self.dfs(combination + letter, digits[1:], result)

   
