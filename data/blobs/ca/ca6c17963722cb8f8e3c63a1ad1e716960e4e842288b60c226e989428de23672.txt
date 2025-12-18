class MergeTwoSortedLists {

    /*
        21. Merge Two Sorted Lists
        https://leetcode.com/problems/merge-two-sorted-lists/description/

        두 링크드 리스트의 요소를 하나의 리스트로 정렬해서 반환
        재귀로 풀이 가능 
        

     */

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null) return list2;
        if (list2 == null) return list1;

        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }

    class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }
}