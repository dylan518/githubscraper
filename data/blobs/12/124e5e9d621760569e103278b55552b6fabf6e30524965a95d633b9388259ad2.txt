package CodingNinjaPOTD;

import com.example.datastructure.skeleton.TreeNode;

// https://leetcode.com/problems/construct-string-from-binary-tree

public class TreeToString_0812 {
	StringBuilder sb = new StringBuilder();
	public String tree2str(TreeNode root) {
		if(root == null) return "";
		function(root);
		return sb.toString();
	}

	void function(TreeNode root)
	{
		if(root == null) return ;
		sb.append(root.val);

		if(root.left != null || root.right != null)
		{
			sb.append("(");
			function(root.left);
			sb.append(")");
		}

		if(root.right != null)
		{
			sb.append("(");
			function(root.right);
			sb.append(")");
		}

	}
}