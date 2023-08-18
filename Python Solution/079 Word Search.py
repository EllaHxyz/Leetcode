from collections import defaultdict

class Solution(object):
    def exist(self, board, word)
        '''
        determine if word exist on board.
        
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        '''
        if self._hasEnoughCharacters(board, word):
            m = len(board)
            n = len(board[0])
            for i in range(m):
                for j in range(n):
                    if self._exist(board, i, j, m, n, word):
                        return True
            return False
        else:
            return False
        
    def _exist(board, i, j, m, n, word):
        '''
        start from position [i,j],
        determine if word exist on board.
        board shape: (m,n).
        
        :rtype: bool
        '''
        #roots
        #case: update word to empty = all word found
        if len(word) == 0:
            return True
        #case: out of boundary position
        if i<0 or i>= m or j<0 or j>=n:
            return False
        #case: str not found
        if board[i][j] != word[0]:
            return False
            
        #search: DFS
        
        #found the first character, store it in temp:
        temp = board[i][j]
        #update board: set that position to a special symbol
        board[i][j] = "."
        #update target word
        next_target = word[1:]
        #perform search: up, down, left, right
        next_result = self._exist(board, i-1, j, m, n, next_target) \  #up
                    or self._exist(board, i+1, j, m, n, next_target) \  #down
                    or self._exist(board, i, j-1, m, n, next_target) \ #left
                    or self._exist(board, i, j+1, m, n, next_target) #right
        #update board back to origin
        board[i][j] = temp
        return next_result
        
    
    def _hasEnoughCharacters(self, board, word):
        '''
        count if board has enough characters for the word
        
        :rtype: bool
        '''
        character_counts = defaultdict(int)
        for ch in word:
            character_counts[ch] += 1
            
        return all(sum(line.count(ch) for line in board) >= count for ch, count in character_counts.items())
         
       
        
        
    
if __name__ == "__main__":
   pass
    
    
                
    
