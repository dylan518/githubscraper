
class Solution {
    public boolean isPalindrome(ListNode h) {
        
     if (h == null || h.next == null) return true;
    
    Stack<Integer> stack = new Stack <Integer>();
    
    ListNode a = h; 
    while (a != null) {
        stack.push(a.val);
        a= a.next;     
    }
   
    while (h != null) {
        if (stack.pop() != h.val) {
            return false;
        }
        else {
            h = h.next;
        }
    }
 
    return true;   
    }
}