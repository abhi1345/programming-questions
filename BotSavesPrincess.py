#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    for x in grid:
        if 'm' in x:
            mrow = x
        if 'p' in x:
            prow = x
    m,p,m1,p1 = mrow.index('m'), prow.index('p'), grid.index(mrow), grid.index(prow)
    
    h, v = "none", "none"
    if m < p:
        h = "RIGHT"
    if m > p:
        h = "LEFT"
    if m1 < p1:
        v = "DOWN"
    if m1 > p1:
        v = "UP"    
    
    
    
    if v != "none":
        for x in range(abs(m1 - p1)):
            print(v)
    
    if h != "none":
        for x in range(abs(m - p)):
            print(h)
            
    
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
