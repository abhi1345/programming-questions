class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isp(s):
            return (s == s[::-1])
        ans = 0
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s)+1:
                temp = s[i:j]
                if isp(temp):
                    #print(temp) #debug statement
                    ans += 1
                j += 1
            i += 1
        return ans
                
