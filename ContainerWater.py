class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        front, back = 0, len(height)-1
        
        maxVol = 0
        
        while front < back:
            currVol = (back-front)*min(height[front], height[back])
            
            maxVol = max(currVol, maxVol)
                
            if height[front] > height[back]:
                back -= 1
            else:
                front += 1
                
        return maxVol
