class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        sign = (x < 0)
        if sign:
            x = -x
        i = 0
        while x:
            i *= 10
            i += x % 10
            x = x//10
        if sign:
            i = -i
        if i < -2**31 or i > (2**31)-1:
            return 0
        return i
