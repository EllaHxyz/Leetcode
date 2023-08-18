class Solution(object):
    def combine(self, n, k):
        '''
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        '''
        #init
        result = []
        #corner case
        if k == 0:
            return result
        if n == 0 :
            raise Exception("no numbers to select from")
        if n < k :
            raise Exception("input errors")
        #root
        if k == 1:
            return [[i+1] for i in range(n)] #select all numbers in the list
        #recursion
        if n > k:
            #[n + (n-1)~(k-1)] + (n-1)~k
            result = [[n] + r for r in self.combine(n-1, k-1)]
                    + self.combine(n-1, k)
        else: #n = k
            #[n + (n-1)~(k-1)]
            result = [[n] + r for r in self.combine(n-1, k-1)]
        
    
if __name__ == "__main__":
   pass
    
    
                
    
