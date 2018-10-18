# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        c = 0
        ptr = ListNode(0)
        output = ptr
        while l1 or l2 or c:
            ptr.next = ListNode(0)
            ptr = ptr.next
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v3 = v1 + v2 + c
            if v3 >= 10:
                c = 1
                v3 = v3 % 10
            else:
                c = 0
            ptr.val = v3
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
            
        return output.next
