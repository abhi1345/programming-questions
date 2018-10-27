class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        
        pointcache = {}
        for point in points:
            pointcache[(point.x, point.y)] = pointcache.get((point.x, point.y), 0)+1
                 
        pointset = list(pointcache.keys())
        nump = len(pointset)
        
        if nump == 1:
            return pointcache[(points[0].x, points[0].y)]
        
        answer = 0
        
        for i in range(nump-1):
            slopes = {}
            
            for j in range(i+1, nump):
                dx, dy = pointset[i][0]-pointset[j][0], pointset[i][1]-pointset[j][1]
                
                if dx == 0:
                    s = '#'
                elif dy == 0:
                    s = 0
                else:
                    s = dy/dx
                    
                slopes[s] = slopes.get(s, 0) + pointcache[pointset[j]]                          
                
            answer = max(answer, pointcache[pointset[i]]+max(slopes.values()))
     
        return answer


