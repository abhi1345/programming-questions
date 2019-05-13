class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #largest product of contiguous subarray
        rev = nums[::-1]
        
        for i in range(1, len(nums)):
            #Only multiply by neighbor if nonzero
            nums[i] *= nums[i - 1] or 1
            rev[i] *= rev[i - 1] or 1
        return max(nums+rev)
        #O(n) time
        #O(n) space
