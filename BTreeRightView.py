# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(root, l, i=0):
    if root:
        l[i] = root.val
        helper(root.left, l, i+1)
        helper(root.right, l, i+1)

def levels(root, i=1):
    if not root:
        return i-1
    if (not root.left) and (not root.right):
        return i
    return max(levels(root.left, i+1), levels(root.right, i+1))

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lev = levels(root)
        l = [0]*lev
        helper(root, l)
        return l
        
