
def removeDuplicates(nums):
    '''
    remove duplicates from sorted array II
    return length of output
    
    :type nums: List[int]
    :rtype: int
    '''
    
    if not nums:
        return 0
    
    #init pointer and counter for duplicates
    prev = nums[0]
    count = 1
    j = 1
    
    for i in range(1, len(nums)):
        if nums[i] == prev:
            count += 1
        else:
            count = 1
            prev = nums[i]
            
        #modify input array to account for duplicates
        if count <= 2:
            nums[j] = nums[i]
            j += 1
    return j
    
'''
In this implementation, we use two pointers, i and j, to iterate through the array. The j pointer keeps track of the position where the next non-duplicate element should be placed in the modified array. The i pointer is used to traverse the original array.

We also keep track of the count of consecutive duplicates. When we encounter a new element (i.e., nums[i] != prev), we reset the count to 1 and update the prev variable to the current element. If the count is less than or equal to 2, we copy the element to the modified array at the position indicated by the j pointer and increment j. If the count is greater than 2, we skip the duplicate element.

Finally, the value of j represents the new length of the modified array after removing duplicates, and the modified array nums contains the elements without duplicates (at most two duplicates for each unique element).
'''
