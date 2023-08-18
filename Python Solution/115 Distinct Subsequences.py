

        
class TreeNode:
    def __init__(self, val, left, right)
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def numDistinct(s, t):
        m, n = len(s), len(t)
        #init dp array with zeros
        dp = [[0] * (n+1) for _ in range(m+1)] #mxn array
        
        #base case: when t is an empty string, there is one subsequence in s that matches an empty string
        for i in range(m+1):
            dp[i][0] = 1
        #base case: when s is an empty string, there are zero match when t is not empty. Not included b/c already init with 0s.
        #for j in range(1, n+1):
        #   dp[0][j]=0
        #base case: when s is non-empty, t is empty, always return 0.
        
        #iterate, start with 2nd string character
        for i in range(1, m+1):
            for j in range(1, n+1):
                #if prev character match, we have two choices:use it or skip it
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                #if prev character don't match, we can only skip it
                dp[i][j] = dp[i-1][j] #find match between s[:i-1] and t[:j]
        
        return dp[m][n]
                    
    
