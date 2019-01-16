def col(l, i):
    for row in l:
        row[i] = 0
    
def row(l, i):
    l[i] = [0]*len(l[0])
    

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        r = set()
        c = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        for i in range(len(matrix)):
            if i in r:
                row(matrix, i)
            
        for j in range(len(matrix[0])):
            if j in c:
                col(matrix, j)
     
