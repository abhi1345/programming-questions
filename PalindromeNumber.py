class Solution:

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        l = len(x)-1
        
        while i < len(x)//2:
            if x[i] != x[l-i]:
                return False
            i += 1
            
        return True
