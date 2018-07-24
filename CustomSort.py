class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        T = list(T)
        S = list(S)
        answer = []
        
        for i in S:
            while i in T:
                T.remove(i)
                answer.append(i)
            if len(T) == 0:
                break
        answer.extend(T)
        
        return ''.join(answer)
        
                
                
        
