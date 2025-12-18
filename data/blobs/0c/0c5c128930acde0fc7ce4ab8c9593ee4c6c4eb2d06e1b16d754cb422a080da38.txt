class TreeNode{
    String name;
    List<TreeNode> child;
    boolean isAlive;
    public TreeNode(String _name,boolean _isAlive){
        name=_name;
        child=new ArrayList<>();
        isAlive=_isAlive;
    }
    public void addChild(TreeNode child){
        this.child.add(child);
    }
}

class ThroneInheritance {
    private TreeNode root;
    Map<String,TreeNode> map;
    public ThroneInheritance(String kingName) {
        TreeNode node=new TreeNode(kingName,true);
        root=node;
        map=new HashMap<>();
        map.put(kingName,root);
    }
    
    public void birth(String parentName, String childName) {
        TreeNode parent=map.get(parentName);
        TreeNode child=new TreeNode(childName,true);
        parent.addChild(child);
        map.put(childName,child);
    }
    
    public void death(String name) {
        TreeNode parent=map.get(name);
        parent.isAlive=false;
    }
    
    public List<String> getInheritanceOrder() {
        List<String> res=new ArrayList<>();
        preOrder(root,res);
        return res;
    }

    public void preOrder(TreeNode node,List<String> li){
        if(node.isAlive) li.add(node.name);
        for(TreeNode t : node.child) preOrder(t,li);
    }
}

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance obj = new ThroneInheritance(kingName);
 * obj.birth(parentName,childName);
 * obj.death(name);
 * List<String> param_3 = obj.getInheritanceOrder();
 */