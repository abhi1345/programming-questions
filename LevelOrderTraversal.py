# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
     
def helper(root, l, i=0):
    if root:
        while len(l) < i+1:
            l.append([])
        l[i].append(root.val)
        helper(root.left, l, i+1)
        helper(root.right, l, i+1)

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        answer = []
        helper(root, answer)
        return answer
        
