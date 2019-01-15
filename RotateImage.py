def helper(l, n):
    if n < 2:
        return l
    
    start = max(0, (len(l)//2) - n//2)
    end = start+n
    
    top, bottom = l[start][start:end], l[end-1][start:end]
    left, right = [i[start] for i in l[start:end]], [i[end-1] for i in l[start:end]]
    
    l[start][start:end] = left[::-1]
    l[end-1][start:end] = right[::-1]
    
    try:
        for i in range(start, end):
            l[i][start] = bottom[i-start]
            l[i][end-1] = top[i-start]
    
        
    
    helper(l, n-2)
    

          
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        helper(matrix, len(matrix))
        
