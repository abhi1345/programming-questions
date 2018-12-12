class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        j = set(J)
        
        i = 0
        
        for c in S:
            i += int(c in j)
                
        return i
        
        
"""

Input: J = "z", S = "ZZ"
Output: 0

Input: J = "aA", S = "aAAbbbb"
Output: 3

"""
