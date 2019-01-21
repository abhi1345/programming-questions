class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str (1.0.1)
        :type version2: str (1.1)
        :rtype: int
        """
        v1, v2 = [int(v) for v in version1.split(".")], [int(v) for v in version2.split(".")]
        
        while v1 and v2:
            c1, c2 = v1[0], v2[0]
            if c1 > c2:
                return 1
            elif c2 > c1:
                return -1
            else:
                v1.pop(0)
                v2.pop(0)

        if v1 and any(v1):
            return 1
        if v2 and any(v2):
            return -1
        
        return 0
