package org.brody.leetcode;

import org.brody.leetcode.base.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * <a href="https://leetcode.cn/problems/binary-tree-inorder-traversal/">94. 二叉树的中序遍历</a>
 * <p>
 * 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
 * <p>
 * 示例 1：
 * <p>
 * 输入：root = [1,null,2,3]
 * 输出：[1,3,2]
 * 示例 2：
 * <p>
 * 输入：root = []
 * 输出：[]
 * 示例 3：
 * <p>
 * 输入：root = [1]
 * 输出：[1]
 * <p>
 * 提示：
 * <p>
 * 树中节点数目在范围 [0, 100] 内
 * -100 <= Node.val <= 100
 * <p>
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 *
 * @author Brody
 * @date 2022/12/21
 */
public class Easy94BinaryTreeInorderTraversal {

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        TreeNode right = new TreeNode(2);
        root.setRight(right);
        TreeNode rightLeft = new TreeNode(3);
        right.setLeft(rightLeft);
        System.out.println(new Easy94BinaryTreeInorderTraversal().inorderTraversal(root));
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        // 前序遍历、中序遍历和后序遍历的前中后是指的根节点的位置，中序遍历是左中右
        List<Integer> result = new ArrayList<>();
        return inorderTraversal(root, result);
    }

    public List<Integer> inorderTraversal(TreeNode root, List<Integer> result) {
        // 前序遍历、中序遍历和后序遍历的前中后是指的根节点的位置，中序遍历是左中右
        if (null == root) {
            return result;
        }
        inorderTraversal(root.left, result);
        result.add(root.val);
        inorderTraversal(root.right, result);
        return result;
    }
}
