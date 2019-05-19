class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        
        for s in strs[1:]:
            i = 0
            x = min(len(ans), len(s))
            while i < x:
                if s[i] != ans[i]:
                    break
                i += 1
            ans = ans[:i]
        
        return ans
