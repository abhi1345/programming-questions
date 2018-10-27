# HELPER FUNCTIONS
def contains(s, l):
    s = s
    for c in s:
        if c not in l:
            return False
    return True

def strtime(h, m):
    hstr = '0' + str(h) if h < 10 else str(h)
    mstr = '0' + str(m) if m < 10 else str(m)
    return hstr + ':' + mstr

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        l = set(list(time))
        
        hour, minute = int(time[:2]), int(time[3:])
        
        if len(l) == 2:
            return time
        
        
        for h in range(hour, hour+24):
            for m in range(minute+1, minute+60):
                
                newh = h
                
                if m >= 60:
                    m -= 60
                    newh = h + 1
                    
                newh = newh%24
                
                currtime = strtime(newh, m)
                
                if contains(currtime, l):
                    return currtime
