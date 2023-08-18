
        
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        #init the arrays to keep track of the max profits for different states
        buy1 = -prices[0]
        sell1 = 0
        buy2 = -prices[0]
        sell2 = 0
        
        for price in prices[1:]:
            #update max profits for the two transactions
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, -price)
        
        return sell2
        
'''you can use dynamic programming to keep track of the maximum profits achievable with up to two transactions at each day. You can break down the problem into four states based on the number of transactions made and whether the stock is currently held or not.'''
            

    
     
