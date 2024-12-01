class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == 0:
        #             nums[i] = nums[j]
        #             nums[j] = 0
        
        left = 0  

        for right in range(len(nums)):
            if nums[right] != 0:
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]
                left += 1    
            
            
        