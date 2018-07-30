class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        
        
        mymap = {}
        
        for i in A:
            
            for j in B:
                
                if i+j in mymap:
                    mymap[i+j] += 1
                    
                else:
                    mymap[i+j] = 1
                    
            
        answer = 0
        
        for h in C:
            
            for j in D:
                
                
                if -h-j in mymap:
                    answer += mymap[-h-j]
                    
                    
        return answer
                    
