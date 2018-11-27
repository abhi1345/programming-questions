class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return S
        peaks = []
        a = b = 0
        
        for i, x in enumerate(S):
            if x == '1':
                b += 1
            else:
                b -= 1
            
            if b == 0:
                peaks.append("1{}0".format(self.makeLargestSpecial(S[a+1: i])))
                a = i+1
                
        peaks.sort(reverse=True)
        return "".join(peaks)
