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
    public List<Double> averageOfLevels(TreeNode root) {
        List<Double> answer = new LinkedList<Double>();
        List<TreeNode> queue = new LinkedList<TreeNode>();
        if (root == null) return answer;
        queue.add(root);
        while (queue.size() > 0) {
            double sum = 0;
            int n = queue.size();
            for (int i=0; i < n; i++) {
                TreeNode curr = queue.get(0);
                sum += curr.val;
                queue.remove(0);
                if (curr.left != null) queue.add(curr.left);
                if (curr.right != null) queue.add(curr.right);
            }
            answer.add(sum/n);
        }
        return answer;
    }
}
