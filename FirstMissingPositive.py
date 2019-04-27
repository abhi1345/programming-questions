class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        for n in nums:
            holder = n
            while holder != 'b' and 0 < holder <= len(nums):
                temp = nums[holder-1]
                nums[holder-1] = 'b'
                holder = temp
                
        for i in range(len(nums)):
            if nums[i] != 'b':
                return i+1
        return len(nums) + 1
