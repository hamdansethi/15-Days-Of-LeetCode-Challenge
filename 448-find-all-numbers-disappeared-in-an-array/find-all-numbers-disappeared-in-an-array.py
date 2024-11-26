class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
    
        nums_set = set(nums)

        x = []
        
        for i in range(1, n+1):
            if(i not in nums):
                x.append(i)
                
        return x
