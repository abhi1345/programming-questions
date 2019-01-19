class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) < num+1:
            res += [n+1 for n in res]
        return res[:num+1]
