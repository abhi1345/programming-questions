class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        s = [asteroids[0]]
    
        for a in asteroids[1:]:
            
            while s and a < 0 < s[-1]:
                if s[-1] < -a:
                    s.pop()
                    
                else:
                    if s[-1] == -a:
                        s.pop()
                    break
                
            else:
                s.append(a)
        
        return s
