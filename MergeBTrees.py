class Solution:
    def mergeTrees(self, t1, t2):
        if t1 is None and t2 is None:
            return None
        
        else:
            
            if t1 is None and not t2 is None:
                t1 = TreeNode(t2.val)
                t1.left = self.mergeTrees(t1.left, t2.left)
                t1.right = self.mergeTrees(t1.right, t2.right)
                
            
            elif not t2 is None and not t1 is None:
                t1.val = t1.val + t2.val
                t1.left = self.mergeTrees(t1.left, t2.left)
                t1.right = self.mergeTrees(t1.right, t2.right)
                
        
        return t1
    
