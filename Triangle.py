class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        
        answers = [0]*len(triangle)
        
        j = len(triangle)-2
        
        while j >= 0:
            for i in range(j+1):
                #j = 2, i = 0
                left_child = triangle[j+1][i]
                right_child = triangle[j+1][i+1]
                triangle[j][i] += min(left_child, right_child)
                
            j -= 1
             
        return triangle[0][0]
