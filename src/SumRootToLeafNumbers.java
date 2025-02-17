//https://leetcode.com/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150
//Level : Medium

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class SumRootToLeafNumbers {
    public int sumNumbers(TreeNode root) {
        String buildNum = "";
        return sumNumbersRcursive(root, buildNum);
    }

    public int sumNumbersRcursive(TreeNode root, String buildNum) {
        if(root == null){
            return 0;
        }
        buildNum += root.val + "";
        if(root.left == null && root.right == null){
            return Integer.valueOf(buildNum);
        }
        return sumNumbersRcursive(root.left, buildNum) + sumNumbersRcursive(root.right, buildNum);
    }
}