class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        while str and str[0] == " ":
            str = str[1:]
        if not str:
            return 0
        first = str[0]
        s = first if first in ("-", "+") else ""
        for c in str[len(s):]:
            try:
                int(c)
                s += c
            except ValueError:
                break
        if not s:
            return 0
        else:
            try:
                return min(max(int(s), -2147483648), 2147483647)
            except ValueError:
                return 0
                
