# Complete the twoStrings function below.
def twoStrings(s1, s2):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    Map = {}
    for i in alpha:
        Map[i] = 0
    
    s1, s2 = list(s1), list(s2)
    s1.sort()
    s2.sort()
    
    for i in s1:
        Map[i]  = 1
        
    for j in s2:
        if Map[j] == 1:
            Map[j] = 2
    
 
    for i in Map.values():
        if i > 1:
            return "YES"
    
    return "NO"
