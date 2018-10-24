class Solution:
    def trap(self, height):
        l = []
        
        fill = 0
        
        for v in height:
            fill = max(fill, v)
            l.append(fill)
            
        drain = 0
        
        i = len(height)-1
        while i >= 0:
            h = height[i]
            
            drain = max(drain, h)
            
            l[i] = min(l[i], drain) - h
            
            i -= 1
            
        return sum(l)
