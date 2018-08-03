class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        r = nums[0]
        
        for i in nums[1:]:
            r ^= i
                  
        t = -r & r
                
        x, y = 0, 0
        
        for i in nums:
            
            if i & t:
                
                x ^= i
                
            else:
                
                y ^= i
                
        return [x,y]
