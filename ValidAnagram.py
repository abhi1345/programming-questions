class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        O(m+n) time, O(m) space
        m = len(s), n = len(t)
        """
        maps = {}
        for char in s:
            if char in maps:
                maps[char] += 1
            else:
                maps[char] = 1
        for char in t:
            if char not in maps or maps[char] == 0:
                return False
            else:
                maps[char] -= 1
        return not any(maps.values())
