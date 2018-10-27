#DFS Approach
def mark(d, grid, i, j, inum):
    if i < len(grid) and j < len(grid[0]) and i >= 0 and j >= 0 and \
        grid[i][j] == '1' and (i,j) not in d:
        d[(i,j)] = inum
        mark(d, grid, i+1, j, inum)
        mark(d, grid, i-1, j, inum)
        mark(d, grid, i, j-1, inum)
        mark(d, grid, i, j+1, inum)
    else:
        return
            
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        visited = {}
        w, h = len(grid[0]), len(grid)
        num = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1' and (i,j) not in visited:
                    mark(visited, grid, i, j, num)
                    num += 1
        return num
        
