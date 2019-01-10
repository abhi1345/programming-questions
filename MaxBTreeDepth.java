/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int maxright = 0;
        int maxleft = 0;
        if ((root.left != null)) {
            maxleft = maxDepth(root.left);
        }
        if ((root.right != null)) {
            maxright = maxDepth(root.right);
        }
        return 1+Math.max(maxleft, maxright);
    }
}
