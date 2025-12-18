class SolutionList {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(left == right || head == null){
            return head;
        }
        ListNode previous = null;
        ListNode current = head;
        for(int i = 0; current != null && i<left-1; i++){
            previous = current;
            current = current.next;
        }
        ListNode last = previous;
        ListNode newEnd = current;

        //reverse between left and right 
        ListNode next = current.next;
        for(int i = 0; current != null && i<right-left+1; i++){
            current.next = previous;
            previous = current;
            current = next;
            if(next != null){
                next = next.next;
            }
        }
        if(last != null){
            last.next = previous;
        }else{
         head = previous;
        }
        newEnd.next = current;

        return head;
        
    }
}
