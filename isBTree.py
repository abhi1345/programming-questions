""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""

def helper(node, c):
    """
    Input: node of a binary tree and a set
    Output: the set + this nodes children (recursively)
    """
    if not node:
        return c
    
    c.add(node.data)
    
    if node.left:
        c.add(node.left.data)
    if node.right:
        c.add(node.right.data)
    
    if not (node.left or node.right):
        return c
    
    else:
        return helper(node.right, c).union(helper(node.left, c))
    

def check_binary_search_tree_(root):
    """
    Input: node of a binary tree
    Output: True/False, indicating if this root and its descendents form a Binary Search Tree
    """
    #Base case
    if not root:
        return True
    
    lset, rset = set(), set()
    left_kids = helper(root.left, lset)
    right_kids = helper(root.right, rset)

    #Checking that all left descendents are less than root
    for l in left_kids:
        if l >= root.data:
            return False
          
    #Checking that all left descendents are less than root
    for r in right_kids:
        if r <= root.data:
            return False
     
    #Left and right nodes must also be BST's
    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)
    
