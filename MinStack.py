class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.e = []
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        minimum = self.getMin()
        if minimum == None or minimum > x:
            minimum = x
        self.e.append((x, minimum))
        

    def pop(self):
        """
        :rtype: void
        """
        self.e.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.e[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.e:
            return self.e[-1][1]
        else:
            return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
