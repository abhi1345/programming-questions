/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    
    private Integer getIndex(RandomListNode head, int l) {
        int i = 0;
        while (head != null) {
            i++;
            head = head.next;
        }
        return l-i;
    }

    private RandomListNode getPointer(RandomListNode head, int i) {
        int j = 0;
        while (j < i) {
            head = head.next;
            j++;
        }
        return head;   
    }
    
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) {
            System.out.println("case1");
            return null;
        } else if (head.next == null) {
            System.out.println("case2");
            RandomListNode answer = new RandomListNode(head.label);
            if (head.random != null) {
                answer.random = answer;
            }
            return answer;
        } else {
            RandomListNode ptr = head;
            int length = 0;
            while (ptr != null) {
                ptr = ptr.next;
                length++;
            }
            RandomListNode ptr2 = head;
            Map<Integer, Integer> pointers = new HashMap<Integer, Integer>();
            RandomListNode deepcopy = new RandomListNode(head.label);
            RandomListNode answer = deepcopy;
            RandomListNode dc = answer;
            ptr2 = ptr2.next;
            pointers.put(0, getIndex(head.random, length));
            int mapindex = 1;
            while (ptr2 != null) {
                pointers.put(mapindex, getIndex(ptr2.random, length));
                deepcopy.next = new RandomListNode(ptr2.label);
                deepcopy = deepcopy.next;
                ptr2 = ptr2.next;
                mapindex++;
            }
            int i = 0;
            while (answer != null) {
                answer.random = getPointer(dc, pointers.get(i));
                answer = answer.next;
                i++;
            }
            return dc;
        }       
    }
}
