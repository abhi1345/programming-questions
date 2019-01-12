def base(s):
    s = list(s)
    s.sort()
    return ''.join(s)

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = {}
        for word in strs:
            if base(word) in ans:
                ans[base(word)].append(word)
            else:
                ans[base(word)] = [word]
        return list(ans.values())
