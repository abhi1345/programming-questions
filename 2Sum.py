#Returns 2 numbers from NUMS that sum to TARGET

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mymap = {}  
        
        for n in range(len(nums)):
            
            if nums[n] in mymap:
                return [mymap[nums[n]], n]
            
            mymap[target-nums[n]] = n
            
        return None
