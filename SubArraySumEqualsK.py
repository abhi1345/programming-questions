from collections import Counter

# Return the number of subarrays of a List<Int> that sum to K

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = Counter()
        sums[0] = 1
        answer, fsum = 0, 0
        for n in nums:
            fsum += n
            if fsum-k in sums:
                answer += sums[fsum-k]
            sums[fsum] += 1
            
        return answer
