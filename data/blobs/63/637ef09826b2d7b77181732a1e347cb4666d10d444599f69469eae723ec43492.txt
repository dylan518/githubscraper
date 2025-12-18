package LinkedList.medium;

public class LL_328 {
    public ListNode oddEvenList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null) return head;

        ListNode oddHead = head.next;

        ListNode odd = oddHead;
        ListNode even = head;
        ListNode preEven = even;

        while(even != null && odd != null){

            if(even.next != null) even.next = even.next.next;
            if(odd.next != null) odd.next = odd.next.next;

            preEven = even;
            even = even.next;
            odd = odd.next;
        }

        if(even != null){
            preEven = even;
        }

        preEven.next = oddHead;
        return head;
    }
}
