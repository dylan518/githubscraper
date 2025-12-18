package List_Node;

/**
 * @Author: IIE
 * @name: Q142_detectCycle
 * @Date: 2024/3/11
 */
public class Q142_detectCycle {
    public ListNode detectCycle(ListNode head){
        ListNode fastNode=new ListNode();
        ListNode slowNode=new ListNode();
        if(head==null||head.next==null){
            return null;
        }else{
            if(head.next.next==null){
                return null;
            }else if(head.next.next==head){
                return head;
            }else{
                fastNode=head.next.next;
                slowNode=head.next;
            }
        }

        //快指针以步长2移动，慢指针以步长1移动
        while(!(fastNode==slowNode||fastNode.next==null||fastNode.next.next==null||slowNode.next==null)){
            fastNode=fastNode.next.next;
            slowNode=slowNode.next;
        }
        if(fastNode==slowNode){
            //找环的入口节点
            //根据数值，慢节点继续移动和头节点移动，最后会相遇在环的入口
            ListNode newNode=head;
            while(newNode!=slowNode){
                newNode=newNode.next;
                slowNode=slowNode.next;
            }
            return slowNode;
        }else{
            return null;
        }
    }
}
