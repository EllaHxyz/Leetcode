class Solution(object):
    def subsets(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        '''
        result = [[]]
        for num in sorted(nums): #Sort list in ascending order - default
            result += [item + [num] for item in result]
        return result
    
if __name__ == "__main__":
    assert Solution().subsets([1,2,3]) == [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
    
    
                
    
