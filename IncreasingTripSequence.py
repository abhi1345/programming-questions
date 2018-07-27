class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        MIN = MID = float('inf')
        
        for n in nums:
            if n <= MIN:
                MIN = n
            elif n <= MID:
                MID = n
            else:
                return True
        return False
        
