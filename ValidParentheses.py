def lsize(l):
    return sum([len(x) for x in l])
    

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stacks = []
        olist, clist = {'(':0, '[':1, '{':2} , {')':0, ']':1, '}':2}
        for p in s:       
            if p in olist:
                index = olist[p]
                opener = True
            else:
                index = clist[p]
                opener = False  
            try:
                if opener:
                    stacks.append(p)
                else:
                    if olist[stacks[-1]] == clist[p]:
                        stacks.pop()
                    else:
                        return False      
            except IndexError:
                return False
            
        return lsize(stacks) == 0
