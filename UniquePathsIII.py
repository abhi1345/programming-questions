def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def dfs(m, i, j, visited, count):
    if not ((0 <= i < len(m)) and (0 <= j < len(m[0]))) or m[i][j] == -1 or (i,j) in visited:
        return 0
    if m[i][j] == 2:
        if len(visited)-1 == count:
            return 1
        else:
            return 0
    ans = 0
    for p in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        c1, c2 = add((i, j), p)
        ans += dfs(m, c1, c2, visited.union(set([(i, j)])), count)
    return ans
            
def find_start(m):
    num = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                a1, a2 = i, j
            if m[i][j] == 0:
                num += 1
    return a1, a2, num
    

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        startx, starty, count = find_start(grid)
        visited = set()
        answer = dfs(grid, startx, starty, visited, count)
        return answer
