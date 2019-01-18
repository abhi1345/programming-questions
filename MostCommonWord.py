import re
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        occ = {}
        
        for word in re.split('\W+', paragraph):
            word = word.lower()
            if word:
                if word in occ:
                    occ[word] += 1
                elif word not in banned:
                    occ[word] = 1
        
        return max(list(occ.keys()), key=lambda x : occ[x])
 
