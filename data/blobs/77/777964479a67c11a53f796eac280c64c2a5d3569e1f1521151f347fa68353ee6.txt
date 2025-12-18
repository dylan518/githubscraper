class Solution {
    List<Integer> a=new ArrayList<>();
    void solve(TreeNode root){
        if(root==null){
            return ;
        }
        solve(root.left);
        a.add(root.val);
        solve(root.right);
    }
    public int kthSmallest(TreeNode root, int k) {
        solve(root);
        return a.get(k-1);

    }
}
