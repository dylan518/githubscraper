package Algorithm.nowcoder.top101;

import Algorithm.structure.TreeNode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class BM41 {
    public List<Integer> rightSideView(TreeNode root){
        List<Integer> res = new ArrayList<>();
        LinkedList<TreeNode> queue = new LinkedList<>();
        if(root==null) return res;
        queue.offer(root);
        while(!queue.isEmpty()){

            int currentLevel = queue.size();
            for (int i = 0; i < currentLevel; i++) {
                TreeNode node = queue.poll();
                if(node.left!=null) queue.offer(node.left);
                if(node.right!=null) queue.offer(node.right);
                if(i==currentLevel-1){
                    res.add(node.val);
                }
            }
        }
        return res;

    }

}
