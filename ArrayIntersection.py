class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m = set(nums1)
        ret = set()
        for n in nums2:
            if n in m:
                ret.add(n)
                
        return list(ret)
    
        #Time: O(n), Space: O(n)
