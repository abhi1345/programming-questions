class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        def help(n):
            if n < 10:
                return True
            
            stringy = str(n)
            
            if '0' in stringy:
                return False
            
            for i in stringy:
                if n % int(i) != 0:
                    return False
                
            return True
        
        return [x for x in range(left, right+1) if help(x)]
                    
