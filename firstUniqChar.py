class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        myset = {}
        
        for char in s:
            if char in myset:
                myset[char] += 1
            else:
                myset[char] = 1
                
        answer = 0
        for char in s:
            if myset[char] == 1:
                return answer
            answer += 1
            
        return -1
