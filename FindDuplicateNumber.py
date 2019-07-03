class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [1,3,4,2,2]: 1 - 3 - 2 - 4 - 2 - 4 (loop)
        [3,1,3,4,2]: 3 - 4 - 2 - 3 - 4 - 2 - 3 - 4 - 2 (loop)
        """
        if len(nums) < 2:
            return -1
        
        tort, hare = nums[0], nums[nums[0]]
        
        while hare != tort:
            tort = nums[tort]
            hare = nums[nums[hare]]
            
        hare = 0
        
        while hare != tort:
            tort, hare = nums[tort], nums[hare]
        
        return tort
        
        
