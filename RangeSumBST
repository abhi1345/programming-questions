# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(root, n, l, r):
    if not root:
        return
    
    if l <= root.val <= r:
        n[0] += root.val
        helper(root.left, n, l, r)
        helper(root.right, n, l, r)
        
    elif root.val > r:
        helper(root.left, n, l, r)
    
    elif root.val < l:
        helper(root.right, n, l, r)
    

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        holder = [0]
        helper(root, holder, L, R)
        return holder[0]
    
