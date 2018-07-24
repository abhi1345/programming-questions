# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        cache = []
        def pit(root):
            try:
                pit(root.left)
            except AttributeError:
                jsfadf = 0
            
            cache.append(root.val)
            
            try:
                pit(root.right)
            except AttributeError:
                jsfadf = 0
        
        pit(root)
        
        return cache
